# arp

> システムのARPキャッシュを表示し、操作します。
> もっと詳しく: <https://manned.org/arp>。

- 現在のARPテーブルを表示する:

`arp -a`

- 特定のエントリを削除([d]elete)する:

`arp -d {{アドレス}}`

- ARPテーブルに新しいエントリを追加([s]et up)する:

`arp -s {{アドレス}} {{macアドレス}}`
