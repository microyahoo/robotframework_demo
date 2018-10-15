#! /usr/bin/env python

# Copyright:   2018 (c) Liang Zheng (zhengliang@xsky.com)

from SSHLibrary import SSHLibrary

USERNAME = "root"
PASSWORD = "redhat"

def issue_cmd_via_root(command, host, username=USERNAME, pwd=PASSWORD, timeout=300, prompt='$ ', sudo=False,  sudo_password=None):
    """
    The return value is ["standard output", "standard error output", return_value]
    """
    sshLib = SSHLibrary()
    try:
        print "[INFO] Begin to open the connection of", str(host)
        sshLib.open_connection(host)
        sshLib.login(username, pwd)
    except SSHClientException:
        print "Could not connect to %s", str(host)
        #TODO setup the OUTPUT env
        sshLib.close_connection()
        return ["", "", -1]
    ret = sshLib.execute_command(command, return_stdout=True, return_stderr=True, return_rc=True, sudo=sudo,  sudo_password=sudo_password) 
    print ret
    sshLib.close_connection()
    return ret

def issue_cmd_via_clish():
    pass

if __name__ == "__main__":
    hostname = "10.0.11.233"
    cmd = "xms-cli --user admin --password admin access-path list"

    issue_cmd_via_root(cmd, hostname)


