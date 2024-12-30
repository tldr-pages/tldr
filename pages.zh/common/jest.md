# jest

> 一个零配置的 JavaScript 测试平台。
> 更多信息：<https://jestjs.io>。

- 运行所有可用的测试：

`jest`

- 从给定文件中运行测试套件：

`jest {{path/to/file1 path/to/file2 ...}}`

- 从当前和子目录中路径匹配给定正则表达式的文件中运行测试套件：

`jest {{regular_expression1}} {{regular_expression2}}`

- 运行名称匹配给定正则表达式的测试：

`jest --testNamePattern {{regular_expression}}`

- 运行与给定源文件相关的测试套件：

`jest --findRelatedTests {{path/to/source_file.js}}`

- 运行与所有未提交文件相关的测试套件：

`jest --onlyChanged`

- 监视文件的更改并自动重新运行相关测试：

`jest --watch`

- 显示帮助：

`jest --help`