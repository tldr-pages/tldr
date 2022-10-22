# aws configure

> AWS CLI の設定を管理します。
> 詳しくはこちら: <https://docs.aws.amazon.com/cli/latest/reference/configure/>.

- 対話形式で AWS CLI を設定する（新しい設定の作成、または既定の更新）:

`aws configure`

- 対話形式で AWS CLI の名前付きプロファイルを設定する（新規プロファイルの作成、または既存プロファイルの更新）:

`aws configure --profile {{プロファイル名}}`

- 特定の設定変数の値を表示する:

`aws configure get {{名前}}`

- 特定プロファイルの設定変数の値を表示する:

`aws configure get {{名前}} --profile {{プロファイル名}}`

- 特定の設定変数の値をセットする:

`aws configure set {{名前}} {{値}}`

- 特定プロファイルの設定変数の値をセットする:

`aws configure set {{名前}} {{値}} --profile {{プロファイル名}}`

- 設定エントリを一覧表示する:

`aws configure list`

- 特定プロファイル内の設定エントリを一覧表示する:

`aws configure list --profile {{プロファイル名}}`
