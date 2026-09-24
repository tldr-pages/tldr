# git for-each-ref

> Gitリポジトリ内の参照 (ブランチ、タグ) を一覧表示し、必要に応じて整形する。
> 詳細情報: <https://git-scm.com/docs/git-for-each-ref>。

- すべての参照 (ブランチとタグ) を一覧表示する:

`git for-each-ref`

- ブランチだけを一覧表示する:

`git for-each-ref refs/heads/`

- タグだけを一覧表示する:

`git for-each-ref refs/tags/`

- `HEAD` にマージ済みのブランチを表示する:

`git for-each-ref --merged HEAD refs/heads/`

- すべての参照の短い名前を一覧表示する:

`git for-each-ref --format "%(refname:short)"`

- 参照をコミット日時で並べ替える (新しいものを先に表示):

`git for-each-ref --sort -committerdate`

- 参照をコミット日時で並べ替える (古いものを先に表示):

`git for-each-ref --sort committerdate`

- 出力する参照数を指定した数に制限する:

`git for-each-ref --count {{件数}}`
