# dolt commit

> 将暂存的更改提交到表。
> 更多信息：<https://docs.dolthub.com/cli-reference/cli#dolt-commit>。

- 提交所有暂存的更改，并打开由 `$EDITOR` 环境变量指定的编辑器来输入提交信息：

`dolt commit`

- 提交所有暂存的更改，并使用指定的提交信息：

`dolt commit --message "{{commit_message}}"`

- 在提交前将所有未暂存的更改暂存到表：

`dolt commit --all`

- 使用指定的 ISO 8601 格式的提交日期（默认为当前日期和时间）：

`dolt commit --date "{{2021-12-31T00:00:00}}"`

- 使用指定的作者信息进行提交：

`dolt commit --author "{{author_name}} <{{author_email}}>"`

- 允许创建没有任何更改的空提交：

`dolt commit --allow-empty`

- 忽略外键警告：

`dolt commit --force`
