# Copyright:   2018 (c) Liang Zheng (zhengliang@xsky.com)

*** Settings ***
Library                SSHLibrary

*** Variables ***
#${HOST_USER}            root
#${HOST_PWD}            redhat


**** Keywords ****
Open Connection And Log In
    [Arguments]    ${host}    ${username}=%{ENV_HOST_USER}    ${password}=%{ENV_HOST_PWD} 
    Open Connection     ${host}
    Login               ${username}        ${password}
