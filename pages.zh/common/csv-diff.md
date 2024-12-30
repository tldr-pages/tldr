# csv-diff

> 查看两个CSV、TSV或JSON文件之间的差异。
> 更多信息：<https://github.com/simonw/csv-diff>。

- 使用特定列作为唯一标识符，显示文件之间差异的可读摘要：

`csv-diff {{path/to/file1.csv}} {{path/to/file2.csv}} --key {{column_name}}`

- 显示文件之间差异的可读摘要，包括在至少有一个变化的行中未更改的值：

`csv-diff {{path/to/file1.csv}} {{path/to/file2.csv}} --key {{column_name}} --show-unchanged`

- 使用特定列作为唯一标识符，以JSON格式显示文件之间差异的摘要：

`csv-diff {{path/to/file1.csv}} {{path/to/file2.csv}} --key {{column_name}} --json`