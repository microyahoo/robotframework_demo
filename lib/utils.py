#! /usr/bin/env python

# Copyright:   2018 (c) Liang Zheng (zhengliang@xsky.com)

import os
import select
import shlex
import subprocess

# the following code logic is taken from ansible source code
def run_command(cmd, environ_update=None, cwd=None, umask=None):
    # print environ_update
 
    args = shlex.split(cmd)
    args = [os.path.expanduser(os.path.expandvars(x)) for x in args if x is not None]
    # print args

    rc = 0

    # Manipulate the environ we'll send to the new process
    old_env_vals = {}
    if environ_update:
        for key, val in environ_update.items():
            old_env_vals[key] = os.environ.get(key, None)
            os.environ[key] = val

    kwargs = dict(
            stdin=None,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
    )
    # store the pwd
    prev_dir = os.getcwd()

    # make sure we're in the right working directory
    if cwd and os.path.isdir(cwd):
        cwd = os.path.abspath(os.path.expanduser(cwd))
        kwargs['cwd'] = cwd
        try:
            os.chdir(cwd)
        except (OSError, IOError) as e:
            print e
            # self.fail_json(rc=e.errno, msg="Could not open %s, %s" % (cwd, to_native(e)),
            #                exception=traceback.format_exc())

    old_umask = None
    if umask:
        old_umask = os.umask(umask)

    try:
        stdout = ''
        stderr = ''

        cmd = subprocess.Popen(args, **kwargs)

        rpipes = [cmd.stdout, cmd.stderr]

        while True:
            rfds, wfds, efds = select.select(rpipes, [], rpipes, 1)
	    stdout += _read_from_pipes(rpipes, rfds, cmd.stdout)
	    stderr += _read_from_pipes(rpipes, rfds, cmd.stderr)
	    # only break out if no pipes are left to read or
	    # the pipes are completely read and
	    # the process is terminated
	    if (not rpipes or not rfds) and cmd.poll() is not None:
		break
	    # No pipes are left to read but process is not yet terminated
	    # Only then it is safe to wait for the process to be finished
	    # NOTE: Actually cmd.poll() is always None here if rpipes is empty
	    elif not rpipes and cmd.poll() is None:
		cmd.wait()
		# The process is terminated. Since no pipes to read from are
		# left, there is no need to call select() again.
		break
        cmd.stdout.close()
        cmd.stderr.close()

        rc = cmd.returncode
    except Exception as e:
        rc = -1
        print e

    # Restore env settings
    for key, val in old_env_vals.items():
        if val is None:
            del os.environ[key]
        else:
            os.environ[key] = val

    if old_umask:
        os.umask(old_umask)

    # reset the pwd
    os.chdir(prev_dir)

    return (rc, stdout, stderr)

def _read_from_pipes(rpipes, rfds, file_descriptor):
    data = ''
    if file_descriptor in rfds:
        data = os.read(file_descriptor.fileno(), 9000)
        if data == '':
            rpipes.remove(file_descriptor)

    return data
