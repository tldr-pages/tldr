# nslookup

> ネームサーバに様々なドメインレコードを問い合わせます。
> もっと詳しく: <https://manned.org/nslookup>。

- システムのデフォルトネームサーバに、ドメインの IP アドレス（A レコード）を問い合わせる:

`nslookup {{example.com}}`

- 指定したネームサーバにドメインの NS レコードを問い合わせる:

`nslookup -type=NS {{example.com}} {{8.8.8.8}}`

- IP アドレスの逆引き（PTR レコード）を問い合わせる:

`nslookup -type=PTR {{54.240.162.118}}`

- TCP プロトコルを使って利用可能なレコードを問い合わせる:

`nslookup -vc -type=ANY {{example.com}}`

- TCP プロトコルを使用して、指定したネームサーバにドメインのゾーンファイル全体を問い合わせる (ゾーン転送):

`nslookup -vc -type=AXFR {{example.com}} {{ネームサーバ}}`

- ドメインのメールサーバ (MX レコード)を照会し、トランザクションの詳細を表示する:

`nslookup -type=MX -debug {{example.com}}`

- 指定したポート番号のネームサーバに、ドメインの TXT レコードを問い合わせる:

`nslookup -port={{ポート番号}} -type=TXT {{example.com}} {{ネームサーバ}}`
