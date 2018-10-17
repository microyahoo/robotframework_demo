Robot Framework Demo
=================================

You can execute the command of "Test_Runner.py test_cases/test.robot" to run test cases.

```
代码目录结构
.
├── README.md
├── Test_Runner.py
├── env
│   ├── bj
│   │   └── bj.yaml
│   ├── common.yaml
│   └── sz
│       └── sz.yaml
├── lib
│   ├── IssueCmd.py
│   ├── MappingGroup.py
│   └── utils.py
├── log.html
├── output.xml
├── report.html
├── resources
│   └── ssh.robot
└── test_cases
    └── test.robot
```
## TODO
1.	异常处理、日志输出
2.	用户友好的使用接口
3.	支持suite级别，或者多个robot files
4.  把测试环境容器化或者tar包
5.	Python多版本支持，跨平台？

## References
  * [Robot Framework][ref-1]
  * [Robot Framework User Guide][ref-2]
  * [SSHLibrary][ref-3]
  * [Robot Framework Quick Start Guide][ref-4]
  * [SSHLibrary keywords][ref-5]
  * [virtualenv][ref-6]
  * [virtualenv User Guide][ref-7]

[ref-1]: http://robotframework.org
[ref-2]: http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html
[ref-3]: https://github.com/robotframework/SSHLibrary
[ref-4]: https://github.com/robotframework/QuickStartGuide/blob/master/QuickStart.rst
[ref-5]: http://robotframework.org/SSHLibrary/SSHLibrary.html
[ref-6]: https://pypi.org/project/virtualenv/
[ref-7]: https://virtualenv.pypa.io/en/stable/userguide/
