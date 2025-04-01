# csvsort

> 对 CSV 文件进行排序。
> 包含在 csvkit 中。
> 更多信息：<https://csvkit.readthedocs.io/en/latest/scripts/csvsort.html>。

- 按第 9 列对 CSV 文件进行排序：

`csvsort -c {{9}} {{data.csv}}`

- 按 "name" 列降序对 CSV 文件进行排序：

`csvsort -r -c {{name}} {{data.csv}}`

- 先按第 2 列，再按第 4 列对 CSV 文件进行排序：

`csvsort -c {{2,4}} {{data.csv}}`

- 不推断数据类型对 CSV 文件进行排序：

`csvsort --no-inference -c {{columns}} {{data.csv}}`
