# tracert

> PCとターゲット間の経路の各ステップに関する情報を受信します。
> もっと詳しく: <https://learn.microsoft.com/windows-server/administration/windows-commands/tracert>。

- ルートを追跡する:

`tracert {{IP}}`

- `tracert`がIPアドレスをホスト名に解決しないようにする:

`tracert /d {{IP}}`

- `tracert`にIPv4のみの利用を強制する:

`tracert /4 {{IP}}`

- `tracert`にIpv6のみの利用を強制する:

`tracert /6 {{IP}}`

- ターゲットの検索における最大ホップ数を指定する:

`tracert /h {{最大ホップ数}} {{IP}}`

- ヘルプを表示する:

`tracert /?`
