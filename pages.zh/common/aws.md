# aws

> Amazon Web Services 的官方 CLI 工具。
> 此命令也有关于其子命令的文件，例如：`s3`.
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/>.

- 配置 AWS 命令行：

`aws configure wizard`

- 使用 SSO 配置 AWS 命令行：

`aws configure sso`

- 获取调用者身份（用于排查权限问题）：

`aws sts get-caller-identity`

- 列出某个区域中的 AWS 资源并以 YAML 格式输出：

`aws dynamodb list-tables --region {{us-east-1}} --output yaml`

- 使用自动提示来辅助完成命令：

`aws iam create-user --cli-auto-prompt`

- 获取某个 AWS 资源的交互式向导：

`aws dynamodb wizard {{新_表}}`

- 生成 JSON CLI 骨架（对基础设施即代码很有用）：

`aws dynamodb update-table --generate-cli-skeleton`

- 显示特定命令的帮助信息：

`aws {{命令}} help`
