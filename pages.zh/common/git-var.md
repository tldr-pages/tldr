# git var

> 打印 Git 逻辑变量的值。
> 请参见 `git config`，它比 `git var` 更受推荐。
> 更多信息：<https://git-scm.com/docs/git-var>。

- 打印 Git 逻辑变量的值：

`git var {{GIT_AUTHOR_IDENT|GIT_COMMITTER_IDENT|GIT_EDITOR|GIT_PAGER}}`

- [l]ist 查看所有 Git 逻辑变量：

`git var -l`