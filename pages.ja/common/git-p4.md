# git p4

> PerforceリポジトリからのインポートとPerforceリポジトリへの送信を行う。
> 詳細情報: <https://git-scm.com/docs/git-p4>。

- Perforce depotを新しいGitリポジトリへクローンする:

`git p4 clone {{ディレクトリ/サブディレクトリ/p4_depot}}`

- Perforceからの変更を現在のGitリポジトリへ同期する:

`git p4 sync {{ディレクトリ/サブディレクトリ/p4_depot}}`

- ローカルコミットを最新のPerforce変更の上にリベースする:

`git p4 rebase`

- Gitの変更をPerforceへ送信する:

`git p4 submit`

- 最新のchangelistだけでなく、Perforceの履歴全体をクローンする:

`git p4 clone {{ディレクトリ/サブディレクトリ/p4_depot}}@all`
