# git for-each-repo

> リポジトリの一覧に対してGitコマンドを実行する。
> 注: このコマンドは実験的であり、今後変更される可能性がある。
> 詳細情報: <https://git-scm.com/docs/git-for-each-repo>。

- ユーザー設定変数 `maintenance.repo` に保存された各リポジトリでメンテナンスを実行する:

`git for-each-repo --config maintenance.repo {{maintenance run}}`

- グローバル設定変数に列挙された各リポジトリで `git pull` を実行する:

`git for-each-repo --config {{グローバル設定変数}} {{pull}}`
