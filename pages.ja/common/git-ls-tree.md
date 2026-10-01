# git ls-tree

> ツリーオブジェクトの内容を一覧表示する。
> 詳細情報: <https://git-scm.com/docs/git-ls-tree>。

- ブランチ上のツリーの内容を一覧表示する:

`git ls-tree {{ブランチ名}}`

- コミット上のツリーの内容を、サブツリーまで再帰的に一覧表示する:

`git ls-tree -r {{コミットハッシュ}}`

- コミット上のツリーのファイル名だけを一覧表示する:

`git ls-tree --name-only {{コミットハッシュ}}`

- 現在のブランチheadのファイル名をツリー構造で出力する (注: `tree --fromfile` はWindowsではサポートされていない):

`git ls-tree -r --name-only HEAD | tree --fromfile`
