# dolt init

> 创建一个空的 Dolt 数据库。
> 更多信息：<https://docs.dolthub.com/cli-reference/cli#dolt-init>。

- 在当前目录中初始化一个新的 Dolt 数据库：

`dolt init`

- 初始化一个新的 Dolt 数据库，并创建一个带有指定元数据的提交：

`dolt init --name "{{name}}" --email "{{email}}" --date "{{2021-12-31T00:00:00}}" -b "{{branch_name}}"`