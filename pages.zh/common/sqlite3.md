# sqlite3

> SQLite 3 的命令行接口，SQLite 是一个独立的、基于文件的嵌入式 SQL 引擎。
> 更多信息：<https://sqlite.org/cli.html>。

- 启动交互式 shell 并创建一个新数据库：

`sqlite3`

- 针对已有的数据库打开交互式 shell：

`sqlite3 {{路径/到/数据库.sqlite3}}`

- 对数据库执行一条 SQL 语句后退出：

`sqlite3 {{路径/到/数据库.sqlite3}} '{{SELECT * FROM 某张表;}}'`
