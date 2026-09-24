# git instaweb

> GitWebサーバーを起動するヘルパー。
> 詳細情報: <https://git-scm.com/docs/git-instaweb>。

- 現在のGitリポジトリ用にGitWebサーバーを起動する:

`git instaweb --start`

- localhostだけで待ち受ける:

`git instaweb --start {{[-l|--local]}}`

- 指定したポートで待ち受ける:

`git instaweb --start {{[-p|--port]}} {{1234}}`

- 指定したHTTP daemonを使用する:

`git instaweb --start {{[-d|--httpd]}} {{lighttpd|apache2|mongoose|plackup|webrick}}`

- Webブラウザも自動起動する:

`git instaweb --start {{[-b|--browser]}}`

- 現在実行中のGitWebサーバーを停止する:

`git instaweb --stop`

- 現在実行中のGitWebサーバーを再起動する:

`git instaweb --restart`
