# usql

> 通用 SQL 数据库的命令行界面。
> 更多信息：<https://github.com/xo/usql>.

- 连接到一个特定的数据库：

`usql {{sqlserver|mysql|postgres|sqlite3|...}}://{{用户名}}:{{密码}}@{{主机}}:{{端口}}/{{数据库名}}`

- 从文件中执行命令：

`usql --file={{路径/到/文件.sql}}`

- 执行一个特定的 SQL 命令：

`usql --command="{{sql命令}}"`

- 在 `usql` 提示符下运行一个 SQL 命令：

`{{prompt}}=> {{sql命令}}`

- 显示数据库架构：

`{{prompt}}=> \d`

- 将查询结果导出到一个特定文件：

`{{prompt}}=> \g {{路径/到/结果文件}}`

- 从 CSV 文件导入数据到一个特定表：

`{{prompt}}=> \copy {{路径/到/data.csv}} {{表名}}`
