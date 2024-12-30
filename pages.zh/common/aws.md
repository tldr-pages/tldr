# aws

> 亚马逊网络服务的官方CLI工具。
> 一些子命令，如`s3`，有自己的使用文档。
> 更多信息：<https://aws.amazon.com/cli>。

- 配置AWS命令行：

`aws configure wizard`

- 使用SSO配置AWS命令行：

`aws configure sso`

- 获取调用者身份（用于故障排除权限）：

`aws sts get-caller-identity`

- 列出区域中的AWS资源并以YAML格式输出：

`aws dynamodb list-tables --region {{us-east-1}} --output yaml`

- 使用自动提示来帮助输入命令：

`aws iam create-user --cli-auto-prompt`

- 为AWS资源获取交互式向导：

`aws dynamodb wizard {{new_table}}`

- 生成JSON CLI骨架（用于基础设施即代码）：

`aws dynamodb update-table --generate-cli-skeleton`

- 显示特定命令的帮助信息：

`aws {{command}} help`