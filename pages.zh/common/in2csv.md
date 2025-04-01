# in2csv

> 将各种表格数据格式转换为 CSV。
> 包含在 csvkit 中。
> 更多信息：<https://csvkit.readthedocs.io/en/latest/scripts/in2csv.html>.

- 将 XLS 文件转换为 CSV：

`in2csv {{data.xls}}`

- 将 DBF 文件转换为 CSV 文件：

`in2csv {{data.dbf}} > {{data.csv}}`

- 将 XLSX 文件中的特定工作表转换为 CSV：

`in2csv --sheet={{sheet_name}} {{data.xlsx}}`

- 将 JSON 文件通过管道传递给 in2csv：

`cat {{data.json}} | in2csv -f json > {{data.csv}}`
