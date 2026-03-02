# choco apikey

> ChocolateyソースのAPIキーを管理します。
> 詳細情報: <https://docs.chocolatey.org/en-us/create/commands/api-key/>。

- ソースとそのAPIキーのリストを表示します:

`choco apikey`

- 特定のソースとそのAPIキーを表示します:

`choco apikey {{[-s|--source]}} "{{ソースURL}}"`

- ソースのAPIキーを設定します:

`choco apikey {{[-s|--source]}} "{{ソースURL}}" {{[-k|--api-key]}} "{{APIキー}}"`

- ソースのAPIキーを削除します:

`choco apikey {{[-s|--source]}} "{{ソースURL}}" --remove`
