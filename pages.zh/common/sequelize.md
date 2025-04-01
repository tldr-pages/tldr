# sequelize

> 适用于 Postgres、MySQL、MariaDB、SQLite 和 Microsoft SQL Server 的基于 Promise 的 Node.js ORM。
> 更多信息：<https://sequelize.org/>.

- 创建一个包含 3 个字段的模型和一个迁移文件：

`sequelize model:generate --name {{table_name}} --attributes {{field1:integer,field2:string,field3:boolean}}`

- 运行迁移文件：

`sequelize db:migrate`

- 回滚所有迁移：

`sequelize db:migrate:undo:all`

- 创建一个指定名称的种子文件以填充数据库：

`sequelize seed:generate --name {{seed_filename}}`

- 使用所有种子文件填充数据库：

`sequelize db:seed:all`
