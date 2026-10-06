# git rev-parse

> リビジョンに関連するメタデータを表示する。
> 詳細情報: <https://git-scm.com/docs/git-rev-parse>。

- ブランチのコミットハッシュを取得する:

`git rev-parse {{ブランチ名}}`

- 現在のブランチ名を取得する:

`git rev-parse --abbrev-ref {{HEAD}}`

- ルートディレクトリへの絶対パスを取得する:

`git rev-parse --show-toplevel`
