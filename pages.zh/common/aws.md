# aws

> Amazon Web Services 的官方命令行工具。
> 一些子命令（如 `s3`）有自己的使用文档。
> 更多信息：<https://aws.amazon.com/cli>.

- 配置 AWS 命令行工具：

`aws configure wizard`

- 使用 SSO 配置 AWS 命令行工具：

`aws configure sso`

- 获取调用者身份（用于排查权限问题）：

`aws sts get-caller-identity`

- 列出指定区域的 AWS 资源，并以 YAML 格式输出：

`aws dynamodb list-tables --region {{us-east-1}} --output yaml`

- 使用自动提示帮助完成命令：

`aws iam create-user --cli-auto-prompt`

- 获取 AWS 资源的交互式向导：

`aws dynamodb wizard {{new_table}}`

- 生成 JSON CLI 骨架（适用于基础架构即代码）：

`aws dynamodb update-table --generate-cli-skeleton`

- 显示特定命令的帮助信息：

`aws {{command}} help`
