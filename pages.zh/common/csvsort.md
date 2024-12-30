# csvsort

> 排序 CSV 文件。
> 包含在 csvkit 中。
> 更多信息：<https://csvkit.readthedocs.io/en/latest/scripts/csvsort.html>。

- 按第 9 列排序 CSV 文件：

`csvsort -c {{9}} {{data.csv}}`

- 按“名称”列降序排序 CSV 文件：

`csvsort -r -c {{name}} {{data.csv}}`

- 按第 2 列排序，然后按第 4 列排序：

`csvsort -c {{2,4}} {{data.csv}}`

- 排序 CSV 文件时不推断数据类型：

`csvsort --no-inference -c {{columns}} {{data.csv}}`