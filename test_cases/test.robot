# Copyright:   2018 (c) Liang Zheng (zhengliang@xsky.com)

*** Settings ***
Documentation          This example demonstrates executing a command on a remote machine
...                    and getting its output.
...
...                    Notice how connections are handled as part of the suite setup and
...                    teardown. This saves some time when executing several test cases.

Library                SSHLibrary
Library                ../lib/IssueCmd.py 
Resource               ../resources/ssh.robot

Suite Teardown         Close All Connections

*** Variables ***
${HOST}                10.0.11.233

*** Test Cases ***
Verify Access Path Output
    [Documentation]    Execute Command can be used to run commands on the remote machine.
    ...                The keyword returns the array of standard output, error output and return value.
    ${output}=         Issue Cmd Via Root    xms-cli --user admin --password admin access-path list   host=${HOST}
    Should Contain    ${output}[0]          access-path3

Verify Volume List Output
    [Documentation]     Test volume list output
    [Setup]             Open Connection And Log In    host=${HOST}
    ${output}=          Execute Command    xms-cli --user admin --password admin block-volume list
    Should Contain      ${output}    testvolume
