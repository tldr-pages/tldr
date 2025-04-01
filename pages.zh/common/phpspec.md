# phpspec

> 一个用于 PHP 的行为驱动开发工具。
> 更多信息：<https://phpspec.net>。

- 为一个类创建规范：

`phpspec describe {{class_name}}`

- 运行 "spec" 目录中的所有规范：

`phpspec run`

- 运行单个规范：

`phpspec run {{path/to/class_specification_file}}`

- 使用特定配置文件运行规范：

`phpspec run -c {{path/to/configuration_file}}`

- 使用特定引导文件运行规范：

`phpspec run -b {{path/to/bootstrap_file}}`

- 禁用代码生成提示：

`phpspec run --no-code-generation`

- 启用伪造返回值：

`phpspec run --fake`
