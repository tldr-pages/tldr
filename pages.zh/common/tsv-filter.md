# tsv-filter

> 通过对单个字段运行测试来过滤TSV文件的行。
> 更多信息：<https://github.com/eBay/tsv-utils#tsv-filter>。

- 打印特定列与给定数字数值相等的行：

`tsv-filter -H --eq {{field_name}}:{{number}} {{path/to/tsv_file}}`

- 打印特定列与给定数字相等/不相等/小于/小于或等于/大于/大于或等于的行：

`tsv-filter --{{eq|ne|lt|le|gt|ge}} {{column_number}}:{{number}} {{path/to/tsv_file}}`

- 打印特定列与给定字符串相等/不相等/属于/不属于的行：

`tsv-filter --str-{{eq|ne|in-fld|not-in-fld}} {{column_number}}:{{string}} {{path/to/tsv_file}}`

- 过滤非空字段：

`tsv-filter --not-empty {{column_number}} {{path/to/tsv_file}}`

- 打印特定列为空的行：

`tsv-filter --invert --not-empty {{column_number}} {{path/to/tsv_file}}`

- 打印满足两个条件的行：

`tsv-filter --eq {{column_number1}}:{{number}} --str-eq {{column_number2}}:{{string}} {{path/to/tsv_file}}`

- 打印至少满足一个条件的行：

`tsv-filter --or --eq {{column_number1}}:{{number}} --str-eq {{column_number2}}:{{string}} {{path/to/tsv_file}}`

- 计数匹配的行，首行视为[H]ead：

`tsv-filter --count -H --eq {{field_name}}:{{number}} {{path/to/tsv_file}}`