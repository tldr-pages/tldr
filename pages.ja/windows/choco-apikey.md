# choco apikey

> ChocolateyソースのAPIキーを管理します。
> もっと詳しく: <https://docs.chocolatey.org/en-us/create/commands/api-key/>。

- ソースとそのAPIキーのリストを表示します:

`choco apikey`

- 特定のソースとそのAPIキーを表示します:

`choco apikey --source "{{ソースURL}}"`

- ソースのAPIキーを設定します:

`choco apikey --source "{{ソースURL}}" --key "{{APIキー}}"`

- ソースのAPIキーを削除します:

`choco apikey --source "{{ソースURL}}" --remove`
