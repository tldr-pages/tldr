# createdb

> 创建 PostgreSQL 数据库。
> 更多信息：<https://www.postgresql.org/docs/current/app-createdb.html>.

- 创建一个当前用户拥有的数据库：

`createdb {{database_name}}`

- 创建一个特定用户拥有的数据库，并附带描述：

`createdb --owner {{username}} {{database_name}} '{{description}}'`

- 从模板创建数据库：

`createdb --template {{template_name}} {{database_name}}`