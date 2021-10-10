# choco info

> Chocolateyのパッケージに関する詳細情報を表示します。
> 詳しくはこちら: <https://chocolatey.org/docs/commands-info>

- 特定のパッケージに関する情報を表示します:

`choco info {{パッケージ}}`

- ローカルパッケージ情報のみを表示します:

`choco info {{パッケージ}} --local-only`

- パッケージ情報を受信するカスタムソースを指定します:

`choco info {{パッケージ}} --source {{ソースURL|エイリアス}}`

- 認証用のユーザー名とパスワードを入力します:

`choco info {{パッケージ}} --user {{ユーザー名}} --password {{パスワード}}`
