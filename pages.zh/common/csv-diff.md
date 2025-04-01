# csv-diff

> 查看两个 CSV、TSV 或 JSON 文件之间的差异。
> 更多信息：<https://github.com/simonw/csv-diff>.

- 使用特定列作为唯一标识符，显示文件之间差异的易读摘要：

`csv-diff {{path/to/file1.csv}} {{path/to/file2.csv}} --key {{column_name}}`

- 包含至少有一处变化的行中的未变化值，显示文件之间差异的易读摘要：

`csv-diff {{path/to/file1.csv}} {{path/to/file2.csv}} --key {{column_name}} --show-unchanged`

- 使用特定列作为唯一标识符，以 JSON 格式显示文件之间的差异摘要：

`csv-diff {{path/to/file1.csv}} {{path/to/file2.csv}} --key {{column_name}} --json`