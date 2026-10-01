# git merge-one-file

> 自明なマージ後に、1つのファイルのマージを解決する。
> 詳細情報: <https://git-scm.com/docs/git-merge-one-file>。

- ファイルの単純なマージ競合を解決する:

`git merge-one-file {{ディレクトリ/サブディレクトリ/ファイル}}`

- `merge-index` でファイルを処理するためのヘルパーとして使用する:

`git merge-index git-merge-one-file {{ディレクトリ/サブディレクトリ/ファイル}}`

- バイナリファイルのマージを処理する:

`git merge-one-file -p {{ディレクトリ/サブディレクトリ/ファイル}}`

- スクリプトによるマージで、`read-tree` の後に適用する:

`git read-tree -m {{ブランチ1}} {{ブランチ2}} && git merge-index git-merge-one-file {{ディレクトリ/サブディレクトリ/ファイル}}`
