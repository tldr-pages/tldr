# 排序

> 对文本文件的行进行排序。
> 更多信息：<https://www.gnu.org/software/coreutils/sort>。

- 按升序排序文件：

`sort {{path/to/file}}`

- 按降序排序文件：

`sort --reverse {{path/to/file}}`

- 以不区分大小写的方式排序文件：

`sort --ignore-case {{path/to/file}}`

- 使用数字而非字母顺序排序文件：

`sort --numeric-sort {{path/to/file}}`

- 按每行的第3个字段数值排序`/etc/passwd`，使用":"作为字段分隔符：

`sort --field-separator={{:}} --key={{3n}} {{/etc/passwd}}`

- 如上所述，但当第3个字段的项相等时，按第4个字段的指数数字排序：

`sort -t {{:}} -k {{3,3n}} -k {{4,4g}} {{/etc/passwd}}`

- 排序文件，仅保留唯一的行：

`sort --unique {{path/to/file}}`

- 排序文件，将输出打印到指定的输出文件（可用于就地排序文件）：

`sort --output={{path/to/file}} {{path/to/file}}`