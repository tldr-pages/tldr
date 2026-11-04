# git mergetool

> マージコンフリクト解決ツールを実行してマージコンフリクトを解決する。
> 詳細情報: <https://git-scm.com/docs/git-mergetool>。

- 既定のマージツールを起動してコンフリクトを解決する:

`git mergetool`

- 有効なマージツールを一覧表示する:

`git mergetool --tool-help`

- 名前で指定したマージツールを起動する:

`git mergetool {{[-t|--tool]}} {{ツール名}}`

- マージツールを起動するたびに確認しない:

`git mergetool {{[-y|--no-prompt]}}`

- GUIマージツールを明示的に使用する (`merge.guitool` 設定変数を参照):

`git mergetool {{[-g|--gui]}}`

- 通常のマージツールを明示的に使用する (`merge.tool` 設定変数を参照):

`git mergetool --no-gui`
