# tsv-filter

> 通过对 TSV 文件中的单个字段运行测试来过滤行。
> 更多信息：<https://github.com/eBay/tsv-utils#tsv-filter>。

- 打印特定列数值等于给定数字的行：

`tsv-filter -H --eq {{field_name}}:{{number}} {{path/to/tsv_file}}`

- 打印特定列数值 [eq]ual/[n]on [e]qual/[l]ess [t]han/[l]ess than or [e]qual/[g]reater [t]han/[g]reater than or [e]qual 于给定数字的行：

`tsv-filter --{{eq|ne|lt|le|gt|ge}} {{column_number}}:{{number}} {{path/to/tsv_file}}`

- 打印特定列字符串 [eq]ual/[n]ot [e]qual/部分包含/不包含给定字符串的行：

`tsv-filter --str-{{eq|ne|in-fld|not-in-fld}} {{column_number}}:{{string}} {{path/to/tsv_file}}`

- 过滤非空字段：

`tsv-filter --not-empty {{column_number}} {{path/to/tsv_file}}`

- 打印特定列为空的行：

`tsv-filter --invert --not-empty {{column_number}} {{path/to/tsv_file}}`

- 打印满足两个条件的行：

`tsv-filter --eq {{column_number1}}:{{number}} --str-eq {{column_number2}}:{{string}} {{path/to/tsv_file}}`

- 打印满足至少一个条件的行：

`tsv-filter --or --eq {{column_number1}}:{{number}} --str-eq {{column_number2}}:{{string}} {{path/to/tsv_file}}`

- 统计匹配行数，将第一行解释为 [H]eader：

`tsv-filter --count -H --eq {{field_name}}:{{number}} {{path/to/tsv_file}}`
