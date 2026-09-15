# git annotate

> ファイルの各行にコミットハッシュと最後の作成者を表示する。
> `git annotate` より `git blame` の使用が推奨される。
> `git annotate` は他のバージョン管理システムに慣れた人向けに提供されている。
> 詳細情報: <https://git-scm.com/docs/git-annotate>。

- 各行の先頭に作成者名とコミットハッシュを付けてファイルを出力する:

`git annotate {{ディレクトリ/サブディレクトリ/ファイル}}`

- 各行の先頭に作成者のメールアドレスとコミットハッシュを付けてファイルを出力する:

`git annotate {{[-e|--show-email]}} {{ディレクトリ/サブディレクトリ/ファイル}}`

- `regex` に一致する行だけを出力する:

`git annotate -L :{{regexp}} {{ディレクトリ/サブディレクトリ/ファイル}}`
