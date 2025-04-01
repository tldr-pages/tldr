# csvkit

> CSV 文件的处理工具包。
> 参见：`csvclean`，`csvcut`，`csvformat`，`csvgrep`，`csvlook`，`csvpy`，`csvsort`，`csvstat`。
> 更多信息：<https://csvkit.readthedocs.io/en/0.9.1/cli.html>。

- 使用自定义分隔符对 CSV 文件运行命令：

`{{command}} -d {{delimiter}} {{path/to/file.csv}}`

- 使用制表符作为分隔符对 CSV 文件运行命令（覆盖 -d 选项）：

`{{command}} -t {{path/to/file.csv}}`

- 使用自定义引用字符对 CSV 文件运行命令：

`{{command}} -q {{quote_char}} {{path/to/file.csv}}`

- 对没有标题行的 CSV 文件运行命令：

`{{command}} -H {{path/to/file.csv}}`