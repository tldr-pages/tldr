# git branch

> 管理分支。
> 更多信息：<https://git-scm.com/docs/git-branch>.

- 列出所有分支（包括本地的和远程的；当前分支以 `*` 突出表示）：

`git branch {{[-a|--all]}}`

- 列出哪些分支在其历史中包含指定的提交记录：

`git branch {{[-a|--all]}} --contains {{提交的哈希值}}`

- 显示当前分支的名称：

`git branch --show-current`

- 基于当前提交创建新分支：

`git branch {{分支名}}`

- 基于指定提交创建新分支：

`git branch {{分支名}} {{提交的哈希值}}`

- 重命名分支（需先切换到其他分支）：

`git branch {{[-m|--move]}} {{旧分支名}} {{新分支名}}`

- 删除本地分支（需先切换到其他分支）：

`git branch {{[-d|--delete]}} {{分支名}}`

- 删除远程分支：

`git push {{远程仓库名}} {{[-d|--delete]}} {{远程分支名}}`
