# git subtree

> 将项目依赖项管理为子项目。
> 更多信息：<https://manpages.debian.org/latest/git-man/git-subtree.1.html>。

- 将一个 Git 仓库添加为子树：

`git subtree add --prefix={{路径/到/目录/}} --squash {{仓库_url}} {{分支_name}}`

- 更新子树仓库到其最新提交：

`git subtree pull --prefix={{路径/到/目录/}} {{仓库_url}} {{分支_name}}`

- 将最近的更改合并到最新的子树提交中：

`git subtree merge --prefix={{路径/到/目录/}} --squash {{仓库_url}} {{分支_name}}`

- 将提交推送到子树仓库：

`git subtree push --prefix={{路径/到/目录/}} {{仓库_url}} {{分支_name}}`

- 从子树的历史中提取新的项目历史：

`git subtree split --prefix={{路径/到/目录/}} {{仓库_url}} -b {{分支_name}}`