# git am

> パッチファイルを適用してコミットを作成する。メールでコミットを受け取る場合に便利。
> 参照: `git format-patch`。
> 詳細情報: <https://git-scm.com/docs/git-am>。

- ローカルのパッチファイルに従って変更を適用し、コミットする:

`git am {{ディレクトリ/サブディレクトリ/ファイル.patch}}`

- リモートのパッチファイルに従って変更を適用し、コミットする:

`curl {{[-L|--location]}} {{https://example.com/file.patch}} | git am`

- パッチファイルの適用処理を中止する:

`git am --abort`

- パッチファイルを可能な限り適用し、失敗したハンクをrejectファイルに保存する:

`git am --reject {{ディレクトリ/サブディレクトリ/ファイル.patch}}`
