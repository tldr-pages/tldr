# git switch

> 在 Git 分支之间切换。需要 Git 版本 2.23 或更高版本。
> 另请参阅 `git checkout`。
> 更多信息：<https://git-scm.com/docs/git-switch>。

- 切换到一个现有的分支：

`git switch {{branch_name}}`

- 创建一个新分支并切换到它：

`git switch --create {{branch_name}}`

- 基于现有提交创建一个新分支并切换到它：

`git switch --create {{branch_name}} {{commit}}`

- 切换到上一个分支：

`git switch -`

- 切换到一个分支并更新所有子模块以匹配：

`git switch --recurse-submodules {{branch_name}}`

- 切换到一个分支并自动将当前分支及任何未提交的更改合并到其中：

`git switch --merge {{branch_name}}`