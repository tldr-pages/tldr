# git var

> Gitの論理変数の値を出力する。
> `git var` より `git config` の使用が推奨される。
> 詳細情報: <https://git-scm.com/docs/git-var>。

- Gitの論理変数の値を出力する:

`git var {{GIT_AUTHOR_IDENT|GIT_COMMITTER_IDENT|GIT_EDITOR|GIT_PAGER}}`

- すべてのGit論理変数を一覧表示する:

`git var -l`
