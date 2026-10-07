# tracert

> PCとターゲット間の経路の各ステップに関する情報を受信します。
> 詳細情報: <https://learn.microsoft.com/windows-server/administration/windows-commands/tracert>。

- ルートを追跡する:

`tracert {{ip_address}}`

- `tracert`がIPアドレスをホスト名に解決しないようにする:

`tracert /d {{ip_address}}`

- `tracert`にIPv4のみの利用を強制する:

`tracert /4 {{ip_address}}`

- `tracert`にIpv6のみの利用を強制する:

`tracert /6 {{ip_address}}`

- ターゲットの検索における最大ホップ数を指定する:

`tracert /h {{最大ホップ数}} {{ip_address}}`

- ヘルプを表示する:

`tracert /?`
