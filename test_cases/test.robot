# Copyright:   2018 (c) Liang Zheng (zhengliang@xsky.com)

*** Settings ***
Documentation          This example demonstrates executing a command on a remote machine
...                    and getting its output.
...
...                    Notice how connections are handled as part of the suite setup and
...                    teardown. This saves some time when executing several test cases.

Library                SSHLibrary
Library                lib/IssueCmd.py 
Resource               resources/ssh.robot

Suite Teardown         Close All Connections

*** Variables ***
${host}                10.0.11.233

*** Test Cases ***
Verify Access Path Output
    [Documentation]    Execute Command can be used to run commands on the remote machine.
    ...                The keyword returns the array of standard output, error output and return value.
    Log    %{ENV_XMS_CLI_USER}
    Log    %{ENV_BJ}
    Log    %{ENV_SZ}
    Log    %{ENV_XMS_CLI_PWD}
    ${output}=         Issue Cmd Via Root    xms-cli --user %{ENV_XMS_CLI_USER} --password %{ENV_XMS_CLI_PWD} access-path list   host=${host}
    Log    %{OUTPUT}
    Should Contain    ${output}[0]          access-path3
    Should Contain    %{OUTPUT}             access-path3

Verify Volume List Output
    [Documentation]     Test volume list output
    [Setup]             Open Connection And Log In    host=${host}
    ${output}=          Execute Command    xms-cli --user %{ENV_XMS_CLI_USER} --password %{ENV_XMS_CLI_PWD} block-volume list
    Should Contain      ${output}    testvolume
