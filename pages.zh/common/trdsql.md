# trdsql

> 在 CSV、LTSV、JSON、YAML 和 TBLN 文件上执行 SQL。
> 更多信息：<https://noborus.github.io/trdsql/>。

- 将多个 JSON 文件中的对象数据转换为带有标题（`-oh`）和双引号的 CSV 文件：

`trdsql -ocsv -oh "SELECT * FROM {{path/to/file/*.json}}" | sed 's/\([^,]*\)/"&"/g' > {{path/to/file.csv}}`

- 将 JSON 列解释为表格，并将对象放入列中（path/to/file.json: `{"list":[{"age":"26","name":"Tanaka"}]}`）：

`trdsql "SELECT * FROM {{path/to/file.json}}::.list`

- 使用第一行作为标题（`-ih`）的多个 CSV 文件中的数据进行复杂 SQL 查询操作：

`trdsql -icsv -ih "SELECT {{column1,column2}} FROM {{path/to/file*.csv}} WHERE column2 != '' ORDER BY column1 GROUP BY column1"`

- 将两个 CSV 文件的内容合并为一个 CSV 文件：

`trdsql "SELECT {{column1,column2}} FROM {{path/to/file1.csv}} UNION SELECT {{column1,column2}} FROM {{path/to/file2.csv}}"`

- 连接到 PostgreSQL 数据库：

`trdsql -driver postgres -dsn "host={{hostname}} port={{5433}} dbname={{database_name}}" "SELECT 1"`

- 从 CSV 文件创建 MySQL 数据库的表数据：

`trdsql -driver mysql -dsn "{{username}}:{{password}}@{{hostname}}/{{database}}" -ih "CREATE TABLE {{table}} ({{column1}} int, {{column2}} varchar(20)) AS SELECT {{column3}} AS {{column1}},{{column2}} FROM {{path/to/header_file.csv}}"`

- 显示压缩日志文件中的数据：

`trdsql -iltsv "SELECT * FROM {{path/to/access.log.gz}}"`