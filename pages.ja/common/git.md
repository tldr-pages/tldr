# git

> 分散型バージョン管理システム。
> いくつかのサブコマンドがあります。例えば `commit`, `add`, `branch`, `checkout`, `push`, などです。
> 詳細情報: <https://git-scm.com/docs/git>。

- Gitのサブコマンドを実行する:

`git {{サブコマンド}}`

- Gitのサブコマンドを、任意のリポジトリのルートパスを指定して実行する:

`git -C {{ディレクトリパス}} {{サブコマンド}}`

- Gitのサブコマンドを、指定された設定値で実行する:

`git -c '{{config.key}}={{値}}' {{サブコマンド}}`

- Git全体のヘルプを見る:

`git --help`

- Gitのサブコマンドのヘルプを見る (例えば `clone`, `add`, `push`, `log`, など):

`git help {{サブコマンド}}`

- Gitのバージョンを確認する:

`git --version`
