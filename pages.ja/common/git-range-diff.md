# git range-diff

> 2つのコミット範囲を比較する (例: ブランチの2つのバージョン)。
> 詳細情報: <https://git-scm.com/docs/git-range-diff>。

- 2つの個別コミットの変更を比較する:

`git range-diff {{コミット1}}^! {{コミット2}}^!`

- 例として対話的リベース後に、共通祖先からのoursとtheirsの変更を比較する:

`git range-diff {{theirs}}...{{ours}}`

- リベース後のコンフリクト解消を確認するため、2つのコミット範囲を比較する:

`git range-diff {{base1}}..{{rev1}} {{base2}}..{{rev2}}`
