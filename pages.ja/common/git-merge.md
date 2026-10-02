# git merge

> ブランチをマージする。
> 詳細情報: <https://git-scm.com/docs/git-merge>。

- 指定したブランチを現在のブランチへマージする:

`git merge {{ブランチ名1 ブランチ名2 ...}}`

- マージメッセージを編集する:

`git merge {{[-e|--edit]}} {{ブランチ名}}`

- ブランチをマージし、マージコミットを作成する:

`git merge --no-ff {{ブランチ名}}`

- コミットを作成せずに、ブランチのマージ結果をステージする:

`git merge --squash {{ブランチ名}}`

- コンフリクトが発生したマージを中止する:

`git merge --abort`

- 指定した戦略を使ってマージする:

`git merge {{[-s|--strategy]}} {{戦略}} {{[-X|--strategy-option]}} {{戦略オプション}} {{ブランチ名}}`
