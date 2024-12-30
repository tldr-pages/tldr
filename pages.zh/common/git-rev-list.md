# git rev-list

> 以逆时间顺序列出修订（提交）。
> 更多信息：<https://git-scm.com/docs/git-rev-list>。

- 列出当前分支上的所有提交：

`git rev-list {{HEAD}}`

- 打印在当前分支上更改（添加/编辑/删除）特定文件的最新提交：

`git rev-list {{-n|--max-count}} 1 HEAD -- {{path/to/file}}`

- 列出比特定日期更新的特定分支上的提交：

`git rev-list --since "{{2019-12-01 00:00:00}}" {{branch_name}}`

- 列出特定提交上的所有合并提交：

`git rev-list --merges {{commit}}`

- 打印自特定标签以来的提交数量：

`git rev-list {{tag_name}}..HEAD --count`