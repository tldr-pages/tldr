# git clean

> Gitで追跡されていないファイルを作業ツリーから削除する。
> 詳細情報: <https://git-scm.com/docs/git-clean>。

- 未追跡ファイルを対話的に削除する:

`git clean {{[-i|--interactive]}}`

- 実際には削除せず、削除対象のファイルを表示する:

`git clean {{[-n|--dry-run]}}`

- すべての未追跡ファイルをただちに強制削除する:

`git clean {{[-f|--force]}}`

- 未追跡のディレクトリを削除する:

`git clean {{[-f|--force]}} -d`

- 指定したパスまたはglobパターンに一致する未追跡ファイルだけを削除する:

`git clean {{[-f|--force]}} -- {{ディレクトリ/サブディレクトリ}} '{{*.ext}}'`

- 指定したパターンに一致するものを除き、未追跡ファイルを削除する:

`git clean {{[-f|--force]}} {{[-e|--exclude]}} '{{*.ext}}' {{[-e|--exclude]}} {{ディレクトリ/サブディレクトリ}}/`

- 未追跡ファイルと無視されたファイル (`.gitignore` と `.git/info/exclude` に記載されたもの) を削除する:

`git clean {{[-f|--force]}} -x`
