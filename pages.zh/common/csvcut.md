# csvcut

> 过滤和裁剪 CSV 文件。类似于 Unix 的 `cut` 命令，但用于表格数据。
> 包含在 csvkit 中。
> 更多信息：<https://csvkit.readthedocs.io/en/latest/scripts/csvcut.html>.

- 打印所有列的索引和名称：

`csvcut -n {{data.csv}}`

- 提取第一列和第三列：

`csvcut -c {{1,3}} {{data.csv}}`

- 提取除第四列外的所有列：

`csvcut -C {{4}} {{data.csv}}`

- 提取名为 "id" 和 "first name" 的列（按此顺序）：

`csvcut -c {{id,"first name"}} {{data.csv}}`