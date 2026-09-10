# git restore

> 作業ツリーのファイルを復元する。Git 2.23以降が必要。
> 参照: `git checkout`, `git reset`。
> 詳細情報: <https://git-scm.com/docs/git-restore>。

- ステージされていないファイルを、ステージ済みのバージョンへ復元する:

`git restore {{ファイルへのパス}}`

- ステージされていないファイルを、指定したコミットのバージョンへ復元する:

`git restore {{[-s|--source]}} {{コミット}} {{ファイルへのパス}}`

- 追跡済みファイルのステージされていない変更をすべて破棄する:

`git restore :/`

- ファイルのステージを解除する:

`git restore {{[-S|--staged]}} {{ファイルへのパス}}`

- すべてのファイルのステージを解除する:

`git restore {{[-S|--staged]}} :/`

- ステージ済みかどうかにかかわらず、ファイルへの変更をすべて破棄する:

`git restore {{[-W|--worktree]}} {{[-S|--staged]}} :/`

- 復元するファイルの部分を対話形式で選択する:

`git restore {{[-p|--patch]}}`
