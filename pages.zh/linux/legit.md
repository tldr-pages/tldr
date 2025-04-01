# legit

> Git 的补充命令行界面。
> 更多信息：<https://frostming.github.io/legit>.

- 切换到指定分支，存储并恢复未暂存的更改：

`git switch {{target_branch}}`

- 同步当前分支，自动合并或变基，并存储和恢复更改：

`git sync`

- 将指定分支推送到远程服务器：

`git publish {{branch_name}}`

- 从远程服务器删除一个分支：

`git unpublish {{branch_name}}`

- 列出所有分支及其发布状态：

`git branches {{glob_pattern}}`

- 从历史记录中移除最后一个提交：

`git undo {{--hard}}`