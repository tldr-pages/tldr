# aws

> Amazon Web Services 官方的命令列介面工具。
> 此命令也有關於其子命令的文件，例如：`aws s3`.
> 更多資訊：<https://aws.amazon.com/cli>.

- 設定 AWS 命令列：

`aws configure wizard`

- 使用 SSO 設定 AWS 命令​​列：

`aws configure sso`

- 查看 AWS 指令​​的說明：

`aws {{AWS指令}} help`

- 取得呼叫者身分（用於排除權限問題）：

`aws sts get-caller-identity`

- 列出某個區域中的 AWS Dynamodb 並以 YAML 輸出：

`aws dynamodb list-tables --region {{區域}} --output yaml`

- 使用自動提示來幫助執行命令，：

`aws iam create-user --cli-auto-prompt`

- 取得 AWS 互動式精靈：

`aws dynamodb wizard {{精靈名稱}}`

- 產生 JSON CLI 骨架（對於基礎設施即程式碼有用）：

`aws dynamodb update-table --generate-cli-skeleton`
