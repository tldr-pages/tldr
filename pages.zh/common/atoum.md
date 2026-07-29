# atoum

> 一个简单、现代、直观的 PHP 单元测试框架。
> 更多信息：<https://atoum.readthedocs.io/en/latest/option_cli.html>。

- 初始化配置文件：

`atoum --init`

- 运行所有测试：

`atoum`

- 使用指定配置文件运行测试：

`atoum {{[-c|--configuration]}} {{路径/到/文件}}`

- 运行特定测试文件：

`atoum {{[-f|--files]}} {{路径/到/文件}}`

- 运行特定目录中的测试：

`atoum {{[-d|--directories]}} {{路径/到/目录}}`

- 运行特定命名空间下的所有测试：

`atoum {{[-ns|--namespaces]}} {{命名空间}}`

- 运行带有特定标签的所有测试：

`atoum {{[-t|--tags]}} {{标签}}`

- 在运行测试之前加载自定义引导文件：

`atoum {{[-bf|--bootstrap-file]}} {{路径/到/文件}}`
