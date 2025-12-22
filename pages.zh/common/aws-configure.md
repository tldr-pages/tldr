# aws configure

> 管理 AWS CLI 的配置。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/configure/>.

- 以交互方式配置 AWS CLI（创建新配置或更新默认配置）：

`aws configure`

- 以交互方式为 AWS CLI 配置一个命名的配置文件（创建新配置文件或更新现有配置文件）：

`aws configure --profile {{配置文件名}}`

- 显示某个特定配置变量的值：

`aws configure get {{变量名}}`

- 显示特定配置文件中某个配置变量的值：

`aws configure get {{变量名}} --profile {{配置文件名}}`

- 设置某个特定配置变量的值：

`aws configure set {{变量名}} {{值}}`

- 在特定配置文件中设置某个配置变量的值：

`aws configure set {{变量名}} {{值}} --profile {{配置文件名}}`

- 列出所有配置项：

`aws configure list`

- 列出特定配置文件的配置项：

`aws configure list --profile {{配置文件名}}`
