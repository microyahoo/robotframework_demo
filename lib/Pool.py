#! /usr/bin/env python

# Copyright:   2018 (c) Liang Zheng (zhengliang@xsky.com)

import json
import utils

def get_pool_id(pool_name, host=None):
    """
    return the block volume id according to the volume name.
    """
    cmd = utils.XMS_CLI_HEADER + "-f json pool list"
    print cmd
    ret = utils.execute_cmd_in_host(cmd, host)
    if ret[2] != 0 or isinstance(ret[0], dict):
        print "[Error] Failed to get pool info. Error message: [{err}]".format(err=ret[1])
        return -1
    try:
        pool_info = json.loads(ret[0])
        pools = pool_info["pools"]
        for p in pools:
            if pool_name == p["name"]:
                return p["id"]
    except Exception as e:
        print "[Error] error message is: " + e.message
    return -1

