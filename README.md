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
│   ├── IssueCmd.pyc
│   ├── MappingGroup.py
│   └── MappingGroup.pyc
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

