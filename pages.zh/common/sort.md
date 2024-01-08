# sort

> 对文本文件的行进行排序。
> 更多信息：<https://www.gnu.org/software/coreutils/sort>.

- 以升序对文件进行排序：

`sort {{路径/到/文件}}`

- 以降序对文件进行排序：

`sort --reverse {{路径/到/文件}}`

- 以不区分大小写的方式对文件进行排序：

`sort --ignore-case {{路径/到/文件}}`

- 用数字而不是字母顺序对文件进行排序：

`sort --numeric-sort {{路径/到/文件}}`

- 按每行的第 3 个字段对 `/etc/passwd` 进行数字排序，使用 “:” 作为字段分隔符：

`sort --field-separator={{:}} --key={{3n}} {{/etc/passwd}}`

- 对一个文件进行排序，只保留唯一的行：

`sort --unique {{路径/到/文件}}`

- 对一个文件进行排序，将输出结果打印到指定的输出文件中（可以用来对一个文件进行原地排序）：

`sort --output={{路径/到/文件}} {{路径/到/文件}}`

- 对带有指数的数字进行排序：

`sort --general-numeric-sort {{路径/到/文件}}`
