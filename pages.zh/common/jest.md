# jest

> 一个零配置的 JavaScript 测试平台。
> 更多信息：<https://jestjs.io>.

- 运行所有可用的测试：

`jest`

- 从指定文件中运行测试套件：

`jest {{路径/到/文件1 路径/到/文件2 ...}}`

- 从当前目录和子目录中路径匹配给定正则表达式的文件运行测试套件：

`jest {{正则表达式1}} {{正则表达式2}}`

- 运行名称匹配给定正则表达式的测试：

`jest --testNamePattern {{正则表达式}}`

- 运行与给定源文件相关的测试套件：

`jest --findRelatedTests {{路径/到/源文件.js}}`

- 运行与所有未提交文件相关的测试套件：

`jest --onlyChanged`

- 监视文件更改并自动重新运行相关测试：

`jest --watch`

- 显示帮助信息：

`jest --help`
