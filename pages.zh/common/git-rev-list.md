# git rev-list

> 列出按时间逆序排列的提交记录。
> 更多信息：<https://git-scm.com/docs/git-rev-list>.

- 列出当前分支上的所有提交：

`git rev-list {{HEAD}}`

- 打印最近一次修改指定文件的提交（在当前分支上添加、编辑或删除）：

`git rev-list {{[-n|--max-count]}} 1 HEAD -- {{path/to/file}}`

- 列出特定分支上比某个特定日期更新的提交：

`git rev-list --since "{{2019-12-01 00:00:00}}" {{branch_name}}`

- 列出特定提交上的所有合并提交：

`git rev-list --merges {{commit}}`

- 打印从特定标签到当前分支 HEAD 的提交数量：

`git rev-list {{tag_name}}..HEAD --count`