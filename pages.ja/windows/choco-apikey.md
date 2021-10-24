# choco-apikey

> ChocolateyソースのAPIキーを管理します。
> 詳しくはこちら: <https://chocolatey.org/docs/commands-apikey>

- ソースとそのAPIキーのリストを表示します:

`choco apikey`

- 特定のソースとそのAPIキーを表示します:

`choco apikey --source "{{ソースURL}}"`

- ソースのAPIキーを設定します:

`choco apikey --source "{{ソースURL}}" --key "{{APIキー}}"`

- ソースのAPIキーを削除します:

`choco apikey --source "{{ソースURL}}" --remove`
