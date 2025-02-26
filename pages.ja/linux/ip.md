# ip

> ルーティング、デバイス、ポリシールーティング、トンネルの表示/操作。
> `address` のようないくつかのサブコマンドには、使用方法についての独自のドキュメントがあります。
> もっと詳しく: <https://www.manned.org/ip.8>。

- インターフェースの詳細情報を表示する:

`ip address`

- 簡単なネットワークレイヤの情報を持つインターフェースを一覧表示する:

`ip -brief address`

- リンク層の簡単な情報を持つインターフェースを一覧表示する:

`ip -brief link`

- ルーティングテーブルを表示する:

`ip route`

- ネイバー(ARP テーブル)を表示する:

`ip neighbour`

- インターフェースを up/down する:

`ip link set {{インターフェース}} {{up|down}}`

- インターフェースにIPアドレスを追加/削除する:

`ip addr add/del {{ip}}/{{mask}} dev {{インターフェース}}`

- デフォルトルートを追加する:

`ip route add default via {{ip}} dev {{インターフェース}}`
