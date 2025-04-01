# dolt sql

> 运行 SQL 查询。多个 SQL 语句必须用分号分隔。
> 更多信息：<https://docs.dolthub.com/cli-reference/cli#dolt-sql>.

- 运行单个查询：

`dolt sql --query "{{INSERT INTO t values (1, 3);}}"`

- 列出所有已保存的查询：

`dolt sql --list-saved`