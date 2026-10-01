# git stash

> ローカルのGit変更を一時領域に退避する。
> 詳細情報: <https://git-scm.com/docs/git-stash>。

- 現在の未コミットの変更を退避する:

`git stash`

- 新しい未追跡ファイルを含め、現在の変更を退避する:

`git stash {{[-u|--include-untracked]}}`

- 変更されたファイルから退避する部分を対話形式で選択する:

`git stash {{[-p|--patch]}}`

- すべてのスタッシュを一覧表示する:

`git stash list`

- スタッシュと、そのスタッシュエントリが作成された時点のコミットとの差分をパッチとして表示する:

`git stash show {{[-p|--patch]}}`

- スタッシュを適用し、コンフリクトが発生しなければスタッシュ一覧から削除する:

`git stash pop`

- 最新のスタッシュを削除する:

`git stash drop`

- すべてのスタッシュを削除する:

`git stash clear`
