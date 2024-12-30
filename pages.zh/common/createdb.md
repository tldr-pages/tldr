# 创建数据库

> 创建一个 PostgreSQL 数据库。
> 更多信息：<https://www.postgresql.org/docs/current/app-createdb.html>。

- 创建一个由当前用户拥有的数据库：

`createdb {{database_name}}`

- 创建一个由特定用户拥有并带有描述的数据库：

`createdb --owner {{username}} {{database_name}} '{{description}}'`

- 从模板创建一个数据库：

`createdb --template {{template_name}} {{database_name}}`