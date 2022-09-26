# git switch

> 切换 Git 分支。要求 Git 版本在 2.23 以上。
> 另请参阅 `git checkout`。
> 更多信息：<https://git-scm.com/docs/git-switch>.

- 切换到一个已有的分支：

`git switch {{分支名字}}`

- 创建并切换到一个新分支：

`git switch --create {{分支名字}}`

- 创建并切换到基于某个提交的新分支：

`git switch --create {{分支名字}} {{指定提交}}`

- 切换到之前的分支：

`git switch -`

- 切换到一个分支，并更新所有匹配的子模块：

`git switch --recurse-submodules {{分支名字}}`

- 切换到一个分支，并和当前分支以及暂未提交的修改进行三方合并：

`git switch --merge {{分支名字}}`
