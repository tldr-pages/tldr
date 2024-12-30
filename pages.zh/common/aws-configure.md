# aws configure

> 管理 AWS CLI 的配置。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/configure/>。

- 交互式配置 AWS CLI（创建新配置或更新默认配置）：

`aws configure`

- 交互式为 AWS CLI 配置命名配置文件（创建新配置文件或更新现有配置文件）：

`aws configure --profile {{profile_name}}`

- 显示特定配置变量的值：

`aws configure get {{name}}`

- 显示特定配置文件中配置变量的值：

`aws configure get {{name}} --profile {{profile_name}}`

- 设置特定配置变量的值：

`aws configure set {{name}} {{value}}`

- 在特定配置文件中设置配置变量的值：

`aws configure set {{name}} {{value}} --profile {{profile_name}}`

- 列出配置条目：

`aws configure list`

- 列出特定配置文件的配置条目：

`aws configure list --profile {{profile_name}}`