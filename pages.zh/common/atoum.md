# atoum

> 一个简单、现代且直观的 PHP 单元测试框架。
> 更多信息：<https://atoum.org>。

- 初始化配置文件：

`atoum --init`

- 运行所有测试：

`atoum`

- 使用指定的 [c]onfiguration 文件运行测试：

`atoum -c {{path/to/file}}`

- 运行特定的测试 [f]ile：

`atoum -f {{path/to/file}}`

- 运行特定 [d]irectory 的测试：

`atoum -d {{path/to/directory}}`

- 在特定名称 [s]pace 下运行所有测试：

`atoum -ns {{namespace}}`

- 运行所有带有特定 [t]ag 的测试：

`atoum -t {{tag}}`

- 在运行测试之前加载自定义引导文件：

`atoum --bootstrap-file {{path/to/file}}`