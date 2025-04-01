# mlr

> Miller 类似于 `awk`、`sed`、`cut`、`join` 和 `sort`，用于处理带名字索引的数据，如 CSV、TSV 和表格 JSON。
> 更多信息：<https://johnkerl.org/miller/doc>.

- 以表格格式美化 CSV 文件：

`mlr --icsv --opprint cat {{example.csv}}`

- 接收 JSON 数据并美化输出：

`echo '{"hello":"world"}' | mlr --ijson --opprint cat`

- 按字段进行字母排序：

`mlr --icsv --opprint sort -f {{field}} {{example.csv}}`

- 按字段进行降序数值排序：

`mlr --icsv --opprint sort -nr {{field}} {{example.csv}}`

- 将 CSV 转换为 JSON，并执行计算和显示这些计算：

`mlr --icsv --ojson put '${{newField1}} = ${{oldFieldA}}/${{oldFieldB}}' {{example.csv}}`

- 接收 JSON 并将输出格式化为垂直 JSON：

`echo '{"hello":"world", "foo":"bar"}' | mlr --ijson --ojson --jvstack cat`

- 过滤压缩的 CSV 文件中的行，将数字视为字符串：

`mlr --prepipe 'gunzip' --csv filter -S '${{fieldName}} =~ "{{regular_expression}}"' {{example.csv.gz}}`