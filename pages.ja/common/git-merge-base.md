# git merge-base

> 2つのコミットのマージベースを見つける。
> 詳細情報: <https://git-scm.com/docs/git-merge-base>。

- 2つのコミットのマージベースを出力する:

`git merge-base {{コミット1}} {{コミット2}}`

- 2つのコミットのマージベースをすべて出力する:

`git merge-base {{[-a|--all]}} {{コミット1}} {{コミット2}}`

- 指定したコミットが別のコミットの履歴上にあるか確認する:

`git merge-base --is-ancestor {{対象コミット}} {{基準コミット}}`
