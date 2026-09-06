# git status

> Git リポジトリ内のファイルの変更状況を表示する。
> 現在の `HEAD`、ステージング領域、作業ツリー、未追跡ファイルの状態を一覧表示する。
> 詳細情報: <https://git-scm.com/docs/git-status>。

- まだコミット対象に追加されていない変更済みファイルを表示する:

`git status`

- 短い形式で表示する:

`git status {{[-s|--short]}}`

- ステージング領域と作業ツリーの変更内容を詳細表示する:

`git status {{[-vv|--verbose --verbose]}}`

- ブランチと追跡情報を表示する:

`git status {{[-b|--branch]}}`

- 短い形式でブランチ情報を表示する:

`git status {{[-sb|--short --branch]}}`

- 現在スタッシュに保存されているエントリ数を表示する:

`git status --show-stash`

- 未追跡ファイルを表示しない:

`git status {{[-uno|--untracked-files=no]}}`
