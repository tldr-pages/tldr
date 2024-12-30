# git branch

> 用于处理分支的主要 Git 命令。
> 更多信息：<https://git-scm.com/docs/git-branch>。

- 列出所有分支（本地和远程；当前分支由 `*` 突出显示）：

`git branch --all`

- 列出包含特定 Git 提交历史的分支：

`git branch --all --contains {{commit_hash}}`

- 显示当前分支的名称：

`git branch --show-current`

- 基于当前提交创建新分支：

`git branch {{branch_name}}`

- 基于特定提交创建新分支：

`git branch {{branch_name}} {{commit_hash}}`

- 重命名分支（在执行此操作之前必须切换到不同的分支）：

`git branch {{-m|--move}} {{old_branch_name}} {{new_branch_name}}`

- 删除本地分支（在执行此操作之前必须切换到不同的分支）：

`git branch {{-d|--delete}} {{branch_name}}`

- 删除远程分支：

`git push {{remote_name}} --delete {{remote_branch_name}}`