# csvsql

> 为CSV文件生成SQL语句或直接在数据库上执行这些语句。
> 包含在csvkit中。
> 更多信息：<https://csvkit.readthedocs.io/en/latest/scripts/csvsql.html>。

- 为CSV文件生成`CREATE TABLE` SQL语句：

`csvsql {{path/to/data.csv}}`

- 将CSV文件导入SQL数据库：

`csvsql --insert --db "{{mysql://user:password@host/database}}" {{data.csv}}`

- 在CSV文件上运行SQL查询：

`csvsql --query "{{select * from 'data'}}" {{data.csv}}`