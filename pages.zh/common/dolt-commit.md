# dolt commit

> 提交已暂存的表更改。
> 更多信息：<https://docs.dolthub.com/cli-reference/cli#dolt-commit>。

- 提交所有已暂存的更改，打开由 `$EDITOR` 指定的编辑器以输入提交消息：

`dolt commit`

- 使用指定的消息提交所有已暂存的更改：

`dolt commit --message "{{commit_message}}"`

- 在提交之前将所有未暂存的更改暂存到表中：

`dolt commit --all`

- 使用指定的 ISO 8601 提交日期（默认为当前日期和时间）：

`dolt commit --date "{{2021-12-31T00:00:00}}"`

- 为提交使用指定的作者：

`dolt commit --author "{{author_name}} <{{author_email}}>"`

- 允许创建一个空提交，没有更改：

`dolt commit --allow-empty`

- 忽略外键警告：

`dolt commit --force`