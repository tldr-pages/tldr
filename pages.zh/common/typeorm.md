# typeorm

> 一个可以在 Node.js、浏览器、Cordova、Ionic、React Native、NativeScript 和 Electron 平台上运行的 JavaScript ORM。
> 更多信息：<https://typeorm.io/>。

- 生成一个新的初始 TypeORM 项目结构：

`typeorm init`

- 创建一个空的迁移文件：

`typeorm migration:create --name {{migration_name}}`

- 创建一个包含更新模式的 SQL 语句的迁移文件：

`typeorm migration:generate --name {{migration_name}}`

- 运行所有待处理的迁移：

`typeorm migration:run`

- 在特定目录中创建一个新的实体文件：

`typeorm entity:create --name {{entity}} --dir {{path/to/directory}}`

- 显示 `typeorm schema:sync` 在默认连接上要执行的 SQL 语句：

`typeorm schema:log`

- 在默认连接上执行特定的 SQL 语句：

`typeorm query {{sql_sentence}}`

- 显示子命令的帮助信息：

`typeorm {{subcommand}} --help`