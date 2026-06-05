# tracert

> PCとターゲット間の経路の各ステップに関する情報を受信します。
> 詳細情報: <https://learn.microsoft.com/windows-server/administration/windows-commands/tracert>。

- ルートを追跡する:

`tracert {{ip}}`

- `tracert`がIPアドレスをホスト名に解決しないようにする:

`tracert /d {{ip}}`

- `tracert`にIPv4のみの利用を強制する:

`tracert /4 {{ip}}`

- `tracert`にIpv6のみの利用を強制する:

`tracert /6 {{ip}}`

- ターゲットの検索における最大ホップ数を指定する:

`tracert /h {{最大ホップ数}} {{ip}}`

- ヘルプを表示する:

`tracert /?`
