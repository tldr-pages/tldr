# mysqlcheck

> 检查和修复 MySQL 表。
> 更多信息：<https://dev.mysql.com/doc/refman/8.0/en/mysqlcheck.html>.

- 检查表：

`mysqlcheck --check {{table}}`

- 检查表并提供访问该表的凭证：

`mysqlcheck --check {{table}} --user {{username}} --password {{password}}`

- 修复表：

`mysqlcheck --repair {{table}}`

- 优化表：

`mysqlcheck --optimize {{table}}`