# Copyright:   2018 (c) Liang Zheng (zhengliang@xsky.com)

*** Settings ***
Library                SSHLibrary

*** Variables ***
${USERNAME}            root
${PASSWORD}            redhat


**** Keywords ****
Open Connection And Log In
    [Arguments]    ${host}    ${username}=${USERNAME}    ${password}=${PASSWORD} 
    Open Connection     ${host}
    Login               ${username}        ${password}
