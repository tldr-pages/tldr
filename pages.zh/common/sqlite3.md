# sqlite3

> SQLite 3的命令行界面，这是一个自包含的基于文件的嵌入式SQL引擎。
> 更多信息：<https://sqlite.org>。

- 使用新数据库启动交互式命令行：

`sqlite3`

- 打开一个针对现有数据库的交互式命令行：

`sqlite3 {{path/to/database.sqlite3}}`

- 针对数据库执行SQL语句然后退出：

`sqlite3 {{path/to/database.sqlite3}} '{{SELECT * FROM some_table;}}'`