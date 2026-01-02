# choco info

> Chocolateyのパッケージに関する詳細情報を表示します。
> もっと詳しく: <https://docs.chocolatey.org/en-us/choco/commands/info/>。

- 特定のパッケージに関する情報を表示します:

`choco info {{パッケージ}}`

- ローカルパッケージ情報のみを表示します:

`choco info {{パッケージ}} {{[-l|--local-only]}}`

- パッケージ情報を受信するカスタムソースを指定します:

`choco info {{パッケージ}} {{[-s|--source]}} {{ソースURL|エイリアス}}`

- 認証用のユーザー名とパスワードを入力します:

`choco info {{パッケージ}} {{[-u|--user]}} {{ユーザー名}} {{[-p|--password]}} {{パスワード}}`
