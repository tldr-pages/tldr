# git prune

> 到達不能なすべてのオブジェクトをオブジェクトデータベースから削除するGitコマンド。
> このコマンドは直接使われることは少なく、多くの場合Git gcから使われる内部コマンドとして使用される。
> 詳細情報: <https://git-scm.com/docs/git-prune>。

- Git pruneで削除される内容を、実際には削除せずに報告する:

`git prune {{[-n|--dry-run]}}`

- 到達不能なオブジェクトを削除し、削除された内容を `stdout` に表示する:

`git prune {{[-v|--verbose]}}`

- 進捗を表示しながら到達不能なオブジェクトを削除する:

`git prune --progress`
