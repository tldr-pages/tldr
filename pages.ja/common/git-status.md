# git status

> Git リポジトリ内のファイルの変更状況を表示する。
> 現在チェックアウトされているコミットと比較して、変更・追加・削除されたファイルを一覧表示する。
> 詳細情報: <https://git-scm.com/docs/git-status>。

- コミット対象にまだ追加されていない未追跡ファイルと変更済みファイルを表示する:

`git status`

- 短い形式で表示する:

`git status {{[-s|--short]}}`

- 短い形式でブランチ情報を表示する:

`git status {{[-sb|--short --branch]}}`

- ステージング済みファイルの変更内容を表示する (`git diff --cached` と同様):

`git status {{[-v|--verbose]}}`

- 追跡済みのすべてのファイルの変更内容を表示する (`git diff HEAD` と同様):

`git status {{[-vv|--verbose --verbose]}}`

- 現在スタッシュに保存されているエントリ数を表示する:

`git status --show-stash`

- 未追跡ファイルを出力に表示しない:

`git status {{[-uno|--untracked-files=no]}}`
