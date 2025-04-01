# bru

> Bruno 的命令行工具，一个用于探索和测试 API 的开源 IDE。
> 更多信息：<https://docs.usebruno.com/bru-cli/overview>.

- 运行当前目录中的所有请求文件：

`bru run`

- 通过指定文件名从当前目录运行单个请求：

`bru run {{file.bru}}`

- 使用环境运行请求：

`bru run --env {{environment_name}}`

- 使用带有变量的环境运行请求：

`bru run --env {{environment_name}} --env-var {{variable_name}}={{variable_value}}`

- 运行请求并将结果收集到输出文件中：

`bru run --output {{path/to/output.json}}`

- 显示帮助：

`bru run --help`
