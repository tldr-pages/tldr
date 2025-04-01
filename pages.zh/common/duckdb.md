# duckdb

> DuckDB 的命令行客户端，DuckDB 是一个进程内分析 SQL 引擎。
> 更多信息：<https://duckdb.org>.

- 启动带有临时内存数据库的交互式 shell：

`duckdb`

- 启动连接到数据库文件的交互式 shell。如果文件不存在，则创建新的数据库：

`duckdb {{path/to/dbfile}}`

- 直接查询 CSV、JSON 或 Parquet 文件：

`duckdb -c "{{SELECT * FROM 'data_source.[csv|csv.gz|json|json.gz|parquet]'}}"`

- 执行 SQL 脚本：

`duckdb -f {{path/to/script.sql}}`

- 在数据库文件上执行查询并保持交互式 shell 打开：

`duckdb {{path/to/dbfile}} -cmd "{{SELECT DISTINCT * FROM tbl}}"`

- 在数据库上执行文件中的 SQL 查询并保持交互式 shell 打开：

`duckdb {{path/to/dbfile}} -init {{path/to/script.sql}}`

- 从 `stdin` 读取 CSV 并将 CSV 写入 `stdout`：

`cat {{path/to/source.csv}} | duckdb -c "{{COPY (FROM read_csv('/dev/stdin')) TO '/dev/stdout' WITH (FORMAT CSV, HEADER)}}"`

- 显示帮助：

`duckdb -help`
