# sqlite-utils

> 用于以多种方式操作 SQLite 数据库的命令行工具。
> 更多信息：<https://sqlite-utils.datasette.io/en/stable/cli.html>.

- 创建数据库：

`sqlite-utils create-database {{path/to/database.db}}`

- 创建表：

`sqlite-utils create-table {{path/to/database.db}} {{table_name}} {{id integer name text height float photo blob --pk id}}`

- 列出表：

`sqlite-utils tables {{path/to/database.db}}`

- 更新或插入记录：

`{{echo '[ {"id": 1, "name": "Linus Torvalds"}, {"id": 2, "name": "Steve Wozniak"}, {"id": 3, "name": "Tony Hoare"} ]'}} | sqlite-utils upsert {{path/to/database.db}} {{table_name}} -槠��pk id}}`

- 查询记录：

`sqlite-utils rows {{path/to/database.db}} {{table_name}}`

- 删除记录：

`sqlite-utils query {{path/to/database.db}} "{{delete from table_name where name = 'Tony Hoare'}}"`

- 删除表：

`sqlite-utils drop-table {{path/to/database.db}} {{table_name}}`

- 显示帮助：

`sqlite-utils -h`