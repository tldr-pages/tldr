# git ls-files

> インデックスと作業ツリー内のファイル情報を表示する。
> 詳細情報: <https://git-scm.com/docs/git-ls-files>。

- 削除されたファイルを表示する:

`git ls-files {{[-d|--deleted]}}`

- 変更および削除されたファイルを表示する:

`git ls-files {{[-m|--modified]}}`

- `.gitignore` などで無視されているファイルも含めて、未追跡ファイルを表示する:

`git ls-files {{[-o|--others]}}`

- `.gitignore` などで無視されているファイルを除き、未追跡ファイルを表示する:

`git ls-files {{[-o|--others]}} --exclude-standard`
