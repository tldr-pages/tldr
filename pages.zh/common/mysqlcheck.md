# mysqlcheck

> 检查和修复 MySQL 表。
> 更多信息：<https://dev.mysql.com/doc/refman/8.0/en/mysqlcheck.html>。

- 检查一个表：

`mysqlcheck --check {{table}}`

- 检查一个表并提供访问凭据：

`mysqlcheck --check {{table}} --user {{username}} --password {{password}}`

- 修复一个表：

`mysqlcheck --repair {{table}}`

- 优化一个表：

`mysqlcheck --optimize {{table}}`