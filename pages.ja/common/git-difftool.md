# git difftool

> 外部diffツールを使ってファイルの変更を表示する。`git diff` と同じオプションと引数を受け付ける。
> 参照: `git diff`。
> 詳細情報: <https://git-scm.com/docs/git-difftool>。

- 利用可能なdiffツールを一覧表示する:

`git difftool --tool-help`

- 既定のdiffツールをMeldに設定する:

`git config --global diff.tool "meld"`

- 既定のdiffツールを使ってステージされた変更を表示する:

`git difftool --staged`

- 指定したツールを使って、指定したコミット以降の変更を表示する:

`git difftool {{[-t|--tool]}} {{opendiff}} {{コミット}}`
