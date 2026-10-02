# git rerere

> マージコンフリクトの解決内容を再利用する。
> 詳細情報: <https://git-scm.com/docs/git-rerere>。

- rerereをグローバルに有効化する:

`git config --global rerere.enabled true`

- ファイルに記録された解決内容を忘れる:

`git rerere forget {{ディレクトリ/サブディレクトリ/ファイル}}`

- 記録された解決内容の状態を確認する:

`git rerere status`
