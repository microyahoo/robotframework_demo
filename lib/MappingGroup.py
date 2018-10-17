#! /usr/bin/env python

# Copyright:   2018 (c) Liang Zheng (zhengliang@xsky.com)

import IssueCmd
import json
import os
import sys
import utils

XMS_CLI_USER = os.environ.get("ENV_XMS_CLI_USER", "admin")
XMS_CLI_PWD = os.environ.get("ENV_XMS_CLI_PWD", "admin")

def _execute_cmd(cmd, host):
    if host is not None:
        ret = IssueCmd.issue_cmd_via_root(cmd, host)
    else:
        rc, stdout, stderr = utils.run_command(cmd)
        ret = [stdout, stderr, rc] 
    return ret


def get_mapping_groups(host=None):
    cmd = "xms-cli --user {user} --password {pwd} -f json mapping-group list".format(user=XMS_CLI_USER, pwd=XMS_CLI_PWD)
    ret = _execute_cmd(cmd, host)
    if ret[2] != 0:
        print "[Error] Failed to get mapping groups information."
        return
    # TODO handle exception
    return json.loads(ret[0])

def get_mapping_group_id_via_access_path(access_path, host=None):
    """
    return a list of mapping group ids for specified access path
    """
    mapping_groups = get_mapping_groups(host)
    mp_list = []
    if mapping_groups is not None and type(mapping_groups) in (dict,) \
        and mapping_groups.has_key("mapping_groups"):
        mp_list = mapping_groups["mapping_groups"]
    ret = []
    try:
        for mp in mp_list:
            if mp["access_path"]["name"] == access_path:
                ret.append(mp["id"])
    except TypeError:
        print "[Error] The mapping group data doesn't contain specified 'key'."
    except Exception as e:
        print "[Error]" + e.message 
    return ret


def get_access_path_id(access_path, host=None):
    cmd = "xms-cli --user " + XMS_CLI_USER + " --password " + XMS_CLI_PWD + " -f '{{range .}}{{println .id}}{{end}}' access-path list -q name.raw:" + access_path
    ret = _execute_cmd(cmd, host)
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
    mp_ids = get_mapping_group_id_via_access_path("access-path3", hostname)
    print mp_ids
    print "----begin to test in localhost"
    ret = get_mapping_groups()
    print type(ret)
    print ret
    access_path_id = get_access_path_id("access-path3")
    print access_path_id
    access_path_id = get_access_path_id("access-path")
    print access_path_id
    mp_ids = get_mapping_group_id_via_access_path("access-path3")
    print mp_ids
