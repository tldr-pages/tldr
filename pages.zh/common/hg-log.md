# hg log

> 显示仓库的修订历史。
> 更多信息：<https://www.mercurial-scm.org/doc/hg.1.html#log>。

- 显示仓库的完整修订历史：

`hg log`

- 以 ASCII 图形显示修订历史：

`hg log --graph`

- 显示与指定模式匹配的文件名的修订历史：

`hg log --include {{pattern}}`

- 显示修订历史，排除与指定模式匹配的文件名：

`hg log --exclude {{pattern}}`

- 显示特定修订的日志信息：

`hg log --rev {{revision}}`

- 显示特定分支的修订历史：

`hg log --branch {{branch}}`

- 显示特定日期的修订历史：

`hg log --date {{date}}`

- 显示特定用户提交的修订：

`hg log --user {{user}}`