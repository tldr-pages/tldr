# git credential-cache

> パスワードを一時的にメモリへ保存するGit認証情報ヘルパー。
> 詳細情報: <https://git-scm.com/docs/git-credential-cache>。

- Gitの認証情報を指定した時間だけ保存する:

`git config credential.helper 'cache --timeout={{秒数}}'`
