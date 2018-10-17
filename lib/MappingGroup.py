#! /usr/bin/env python

# Copyright:   2018 (c) Liang Zheng (zhengliang@xsky.com)

import json
import os
import sys
import IssueCmd

XMS_CLI_USER = os.environ.get("ENV_XMS_CLI_USER", "admin")
XMS_CLI_PWD = os.environ.get("ENV_XMS_CLI_PWD", "admin")

def get_mapping_groups(host=None):
    cmd = "xms-cli --user {user} --password {pwd} -f json mapping-group list".format(user=XMS_CLI_USER, pwd=XMS_CLI_PWD)
    if host is not None:
        ret = IssueCmd.issue_cmd_via_root(cmd, host)
    else:
        # TODO run in local env
        pass
    if ret[2] != 0:
        print "[Error] Failed to get mapping groups information."
        return
    # TODO handle exception
    return json.loads(ret[0])

def get_mapping_group_id_via_access_path(access_path, host=None):
    mapping_groups = get_mapping_groups(host)


def get_access_path_id(access_path, host=None):
    cmd = "xms-cli --user " + XMS_CLI_USER + " --password " + XMS_CLI_PWD + " -f '{{range .}}{{println .id}}{{end}}' access-path list -q name.raw:" + access_path
    if host is not None:
        ret = IssueCmd.issue_cmd_via_root(cmd, host)
    else:
        # TODO run in local env
        pass
    if ret[2] != 0:
        print "[Error] Failed to get mapping groups information."
        return
    if ret[0] is None or len(ret[0]) == 0:
        return -1
    # TODO handle exception
    return int(ret[0])


if __name__ == "__main__":
    hostname = "10.0.11.233"
    ret = get_mapping_groups(hostname)
    print type(ret)
    print ret
    access_path_id = get_access_path_id("access-path3", hostname)
    print access_path_id
    access_path_id = get_access_path_id("access-path", hostname)
    print access_path_id
    
