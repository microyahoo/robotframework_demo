#! /usr/bin/env python

# Copyright:   2018 (c) Liang Zheng (zhengliang@xsky.com)

import os
import sys
from SSHLibrary import SSHLibrary

# parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, os.path.abspath(__file__))
# sys.path.insert(0, parentdir)

HOST_USER= "root"
HOST_PWD= "redhat"

def issue_cmd_via_root(command, host, username=HOST_USER, pwd=HOST_PWD, timeout=300, prompt='$ ', sudo=False,  sudo_password=None):
    """
    The return value is ["standard output", "error output", return_value]
    """
    sshLib = SSHLibrary()
    try:
        print "[INFO] Begin to open the connection of", str(host)
        sshLib.open_connection(host)
        sshLib.login(username, pwd)
    except SSHClientException:
        errmsg = "Could not connect to %s", str(host)
        print errmsg
        os.environ["OUTPUT"] = errmsg
        sshLib.close_connection()
        return ["", "", -1]
    ret = sshLib.execute_command(command, return_stdout=True, return_stderr=True, return_rc=True, sudo=sudo,  sudo_password=sudo_password) 
    print ret
    sshLib.close_connection()
    if ret[2] == 0:
        os.environ["OUTPUT"] = ret[0]
    else:
        os.environ["OUTPUT"] = ret[1]
    return ret

def issue_cmd_via_clish():
    pass

if __name__ == "__main__":
    hostname = "10.0.11.233"
    cmd = "xms-cli --user admin --password admin access-path list"

    issue_cmd_via_root(cmd, hostname)
    print __file__

    parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, os.path.abspath(__file__))
    sys.path.insert(0, parentdir)
    print parentdir
    print sys.path

