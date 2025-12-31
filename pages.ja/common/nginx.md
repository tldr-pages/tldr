# nginx

> Nginx ウェブサーバ。
> もっと詳しく: <https://nginx.org/docs/switches.html>。

- デフォルトの設定ファイルでサーバーを起動する:

`nginx`

- カスタム設定ファイルでサーバを起動する:

`nginx -c {{設定ファイル}}`

- 設定ファイル内の全ての相対パスのプレフィクスを指定して、サーバを起動する:

`nginx -c {{設定ファイル}} -p {{prefix/for/relative/paths}}`

- 実行中のサーバに影響を与えずに設定をテストする:

`nginx -t`

- ダウンタイムなしでシグナルを送って、設定をリロードする:

`nginx -s reload`
