# git update-ref

> Git参照の作成、更新、削除を行うGitコマンド。
> 詳細情報: <https://git-scm.com/docs/git-update-ref>。

- 参照を削除する (最初のコミットをソフトリセットする場合に便利):

`git update-ref -d {{HEAD}}`

- メッセージ付きで参照を更新する:

`git update-ref -m {{メッセージ}} {{HEAD}} {{4e95e05}}`
