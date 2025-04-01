# atoum

> 一个简单、现代且直观的 PHP 单元测试框架。
> 更多信息：<https://atoum.readthedocs.io/en/latest/option_cli.html>.

- 初始化配置文件：

`atoum --init`

- 运行所有测试：

`atoum`

- 使用指定的配置文件运行测试：

`atoum {{[-c|--configuration]}} {{path/to/file}}`

- 运行特定的测试文件：

`atoum {{[-f|--files]}} {{path/to/file}}`

- 运行特定目录下的测试：

`atoum {{[-d|--directories]}} {{path/to/directory}}`

- 运行特定命名空间下的所有测试：

`atoum {{[-ns|--namespaces]}} {{namespace}}`

- 运行带有特定标签的所有测试：

`atoum {{[-t|--tags]}} {{tag}}`

- 在运行测试前加载自定义的启动文件：

`atoum {{[-bf|--bootstrap-file]}} {{path/to/file}}`
