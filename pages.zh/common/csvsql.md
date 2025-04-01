# csvsql

> 为 CSV 文件生成 SQL 语句，或直接在数据库上执行这些语句。
> 包含在 csvkit 中。
> 更多信息：<https://csvkit.readthedocs.io/en/latest/scripts/csvsql.html>。

- 为 CSV 文件生成 `CREATE TABLE` SQL 语句：

`csvsql {{path/to/data.csv}}`

- 将 CSV 文件导入 SQL 数据库：

`csvsql --insert --db "{{mysql://user:password@host/database}}" {{data.csv}}`

- 在 CSV 文件上运行 SQL 查询：

`csvsql --query "{{select * from 'data'}}" {{data.csv}}`
