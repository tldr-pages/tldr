# git stripspace

> `stdin` からテキスト (コミットメッセージ、ノート、タグ、ブランチ説明など) を読み取り、Gitで使われる形式に整える。
> 詳細情報: <https://git-scm.com/docs/git-stripspace>。

- ファイルから空白を取り除く:

`cat {{ディレクトリ/サブディレクトリ/ファイル}} | git stripspace`

- ファイルから空白とGitコメントを取り除く:

`cat {{ディレクトリ/サブディレクトリ/ファイル}} | git stripspace {{[-s|--strip-comments]}}`

- ファイル内のすべての行をGitコメントに変換する:

`git < {{ディレクトリ/サブディレクトリ/ファイル}} stripspace {{[-c|--comment-lines]}}`
