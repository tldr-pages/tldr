# aws

> アマゾンウェブサービスの公式 CLI ツールです。
> `aws S3` のようないくつかのサブコマンドには、使用方法についての独自のドキュメントがあります。
> 詳しくはこちら: <https://aws.amazon.com/cli>.

- AWS コマンドラインを設定する:

`aws configure wizard`

- SSO を利用して AWS コマンドラインを設定する:

`aws configure sso`

- AWS コマンドのヘルプを参照する:

`aws {{コマンド}} help`

- 操作呼び出しに使用した認証情報の取得（パーミッションのトラブルシューティングに使用します）:

`aws sts get-caller-identity`

- リージョン内の AWS リソースをリストアップし、YAML で出力する:

`aws dynamodb list-tables --region {{us-east-1}} --output yaml`

- 自動プロンプトを使用してコマンドを補助する:

`aws iam create-user --cli-auto-prompt`

- AWS リソースの対話型ウィザードを取得する:

`aws dynamodb wizard {{新しいテーブル}}`

- JSON CLI スケルトンを生成する（Infrastructure as Code に役立ちます）:

`aws dynamodb update-table --generate-cli-skeleton`
