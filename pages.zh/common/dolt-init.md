# dolt init

> 创建一个新的空的 Dolt 数据库。
> 更多信息：<https://docs.dolthub.com/cli-reference/cli#dolt-init>。

- 在当前目录中初始化一个新的 Dolt 数据库：

`dolt init`

- 初始化一个新的 Dolt 数据库，并使用指定的元数据创建一个提交：

`dolt init --name "{{name}}" --email "{{email}}" --date "{{2021-12-31T00:00:00}}" -b "{{branch_name}}"`
