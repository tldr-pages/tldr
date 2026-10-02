# git reflog

> `HEAD`、ブランチ、タグなどのローカル参照の変更履歴を表示する。
> 詳細情報: <https://git-scm.com/docs/git-reflog>。

- `HEAD` のreflogを表示する:

`git reflog`

- 指定したブランチのreflogを表示する:

`git reflog {{ブランチ名}}`

- reflogの最新5件だけを表示する:

`git reflog {{[-n|--max-count]}} 5`
