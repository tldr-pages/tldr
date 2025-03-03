# ufw

> シンプルなファイアウォール。
> ファイアウォールの設定を簡単にすることを目的とした `iptables` のフロントエンドです。
> もっと詳しく: <https://wiki.ubuntu.com/UncomplicatedFirewall>。

- ufw を有効化:

`ufw enable`

- ufw を無効化:

`ufw disable`

- ufw ルールを、番号と共に表示する:

`ufw status numbered`

- このホストのポート 5432 へのトラフィックを、サービスを識別するコメント付きで許可:

`ufw allow {{5432}} comment "{{Service}}"`

- 192.168.0.4 からこのホストの任意のアドレスへのポート 22 の TCP トラフィックのみを許可:

`ufw allow proto {{tcp}} from {{192.168.0.4}} to {{any}} port {{22}}`

- このホストのポート 80 のトラフィックを拒否:

`ufw deny {{80}}`

- 8412:8500 の範囲のポートへの全ての UDP トラフィックを拒否:

`ufw deny proto {{udp}} from {{any}} to {{any}} port {{8412:8500}}`

- 特定のルールを削除する。ルール番号は `ufw status numbered` コマンドで取得できる:

`ufw delete {{ルール番号}}`
