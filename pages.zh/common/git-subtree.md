# git subtree

> 管理项目依赖项作为子项目。
> 更多信息：<https://manpages.debian.org/latest/git-man/git-subtree.1.html>。

- 将 Git 仓库添加为子树：

`git subtree add --prefix={{path/to/directory/}} --squash {{repository_url}} {{branch_name}}`

- 将子树仓库更新到最新提交：

`git subtree pull --prefix={{path/to/directory/}} {{repository_url}} {{branch_name}}`

- 将最新的子树提交中的最新更改合并到子树中：

`git subtree merge --prefix={{path/to/directory/}} --squash {{repository_url}} {{branch_name}}`

- 将提交推送到子树仓库：

`git subtree push --prefix={{path/to/directory/}} {{repository_url}} {{branch_name}}`

- 从子树的历史中提取新的项目历史：

`git subtree split --prefix={{path/to/directory/}} {{repository_url}} -b {{branch_name}}`