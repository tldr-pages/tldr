# textql

> 对类似 CSV 或 TSV 文件的结构化文本执行 SQL 查询。
> 更多信息：<https://github.com/dinedal/textql>。

- 在指定的 CSV 文件中，将与 SQL 查询匹配的行打印到 `stdout`：

`textql -sql "{{SELECT * FROM filename}}" {{path/to/filename.csv}}`

- 查询 TSV 文件：

`textql -dlm=tab -sql "{{SELECT * FROM filename}}" {{path/to/filename.tsv}}`

- 查询带有标题行的文件：

`textql -dlm={{delimiter}} -header -sql "{{SELECT * FROM filename}}" {{path/to/filename.csv}}`

- 从 `stdin` 读取数据：

`cat {{path/to/file}} | textql -sql "{{SELECT * FROM stdin}}"`

- 在指定的公共列上连接两个文件：

`textql -header -sql "SELECT * FROM {{path/to/file1}} JOIN {{file2}} ON {{path/to/file1}}.{{c1}} = {{file2}}.{{c1}} LIMIT {{10}}" -output-header {{path/to/file1.csv}} {{path/to/file2.csv}}`

- 使用输出分隔符和输出标题行格式化输出：

`textql -output-dlm={{delimiter}} -output-header -sql "SELECT {{column}} AS {{alias}} FROM {{filename}}" {{path/to/filename.csv}}`