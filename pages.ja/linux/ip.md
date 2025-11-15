# ip

> ルーティング、デバイス、ポリシールーティング、トンネルの表示/操作。
> `address` のようないくつかのサブコマンドには、使用方法についての独自のドキュメントがあります。
> もっと詳しく: <https://manned.org/ip.8>。

- インターフェースの詳細情報を表示する:

`ip {{[a|address]}}`

- 簡単なネットワークレイヤの情報を持つインターフェースを一覧表示する:

`ip {{[-br a|-brief address]}}`

- リンク層の簡単な情報を持つインターフェースを一覧表示する:

`ip {{[-br l|-brief link]}}`

- ルーティングテーブルを表示する:

`ip {{[r|route]}}`

- ネイバー(ARP テーブル)を表示する:

`ip {{[n|neighbour]}}`

- インターフェースを up/down する:

`sudo ip {{[l|link]}} {{[s|set]}} {{インターフェース}} {{up|down}}`

- インターフェースに IP アドレスを追加/削除する:

`sudo ip {{[a|address]}} {{add|delete}} {{ip}}/{{mask}} dev {{インターフェース}}`

- デフォルトルートを追加する:

`sudo ip {{[r|route]}} {{[a|add]}} default via {{ip}} dev {{インターフェース}}`
