# sqlite3

> SQLite 3 的命令行接口，它是一个自包含的基于文件的嵌入式 SQL 引擎。
> 更多信息：<https://sqlite.org>。

- 启动与新数据库的交互式 shell：

`sqlite3`

- 打开与现有数据库的交互式 shell：

`sqlite3 {{path/to/database.sqlite3}}`

- 对数据库执行 SQL 语句后退出：

`sqlite3 {{path/to/database.sqlite3}} '{{SELECT * FROM some_table;}}'`
