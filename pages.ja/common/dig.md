# dig

> DNS 情報を調べるユーティリティーです。
> 詳しくはこちら: <https://manned.org/dig>

- ホスト名に関連する IP を検索（A レコード）:

`dig +short {{example.com}}`

- 指定したドメインの詳細な回答を得る（A レコード）:

`dig +noall +answer {{example.com}}`

- 指定されたドメイン名に関連する特定の DNS レコードタイプを取得する:

`dig +short {{example.com}} {{A|MX|TXT|CNAME|NS}}`

- 指定したドメイン名のすべてのタイプのレコードを取得する:

`dig {{example.com}} ANY`

- 問い合わせる別の DNS サーバーを指定する:

`dig @{{8.8.8.8}} {{example.com}}`

- IP アドレスの DNS 逆引きの実行（PTR レコード）:

`dig -x {{8.8.8.8}}`

- ゾーンの権威ネームサーバーの検索と SOA レコードの表示:

`dig +nssearch {{example.com}}`

- ドメイン名を解決するための反復的なクエリの実行と、そのトレースパス全体を表示する:

`dig +trace {{example.com}}`
