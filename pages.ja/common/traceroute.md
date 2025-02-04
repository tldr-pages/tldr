# traceroute

> ネットワークホストへの経路パケット追跡を表示します。
> もっと詳しく: <https://manned.org/traceroute>。

- ホストへの経路追跡:

`traceroute {{example.com}}`

- IPアドレスとホスト名のマッピングを無効化する:

`traceroute -n {{example.com}}`

- 応答までの待機時間を秒単位で指定する:

`traceroute --wait={{0.5}} {{example.com}}`

- ホップごとのクエリ回数を指定する:

`traceroute --queries={{5}} {{example.com}}`

- プローブパケットのサイズをバイト単位で指定する:

`traceroute {{example.com}} {{42}}`

- 宛先までのMTUを特定する:

`traceroute --mtu {{example.com}}`

- UDPの代わりにICMPを使ってトレースルートする:

`traceroute --icmp {{example.com}}`
