# csvstat

> 打印 CSV 文件中所有列的描述性统计信息。
> 包含在 csvkit 中。
> 更多信息：<https://csvkit.readthedocs.io/en/latest/scripts/csvstat.html>.

- 显示所有列的所有统计信息：

`csvstat {{data.csv}}`

- 显示第 2 列和第 4 列的所有统计信息：

`csvstat -c {{2,4}} {{data.csv}}`

- 显示所有列的总和：

`csvstat --sum {{data.csv}}`

- 显示第 3 列的最大值长度：

`csvstat -c {{3}} --len {{data.csv}}`

- 显示 "name" 列中唯一值的数量：

`csvstat -c {{name}} --unique {{data.csv}}`