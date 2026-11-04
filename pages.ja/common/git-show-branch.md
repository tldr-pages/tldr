# git show-branch

> ブランチとそのコミットを表示する。
> 詳細情報: <https://git-scm.com/docs/git-show-branch>。

- ブランチの最新コミットの概要を表示する:

`git show-branch {{ブランチ名|参照|コミット}}`

- 複数のコミットまたはブランチの履歴にあるコミットを比較する:

`git show-branch {{ブランチ名1|参照1|コミット1 ブランチ名2|参照2|コミット2 ...}}`

- すべてのリモート追跡ブランチを比較する:

`git show-branch {{[-r|--remotes]}}`

- ローカルとリモートの両方の追跡ブランチを比較する:

`git show-branch {{[-a|--all]}}`

- すべてのブランチの最新コミットを一覧表示する:

`git show-branch {{[-a|--all]}} --list`

- 指定したブランチと現在のブランチを比較する:

`git show-branch --current {{コミット|ブランチ名|参照}}`

- 相対名の代わりにコミット名を表示する:

`git show-branch --sha1-name --current {{現在|ブランチ名|参照}}`

- 共通の祖先より前のコミットを指定した数だけ表示する:

`git show-branch --more {{5}} {{ブランチ名1|参照1|コミット1 ブランチ名2|参照2|コミット2 ...}}`
