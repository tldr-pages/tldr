# csvkit

> CSV文件的操作工具包。
> 另见：`csvclean`、`csvcut`、`csvformat`、`csvgrep`、`csvlook`、`csvpy`、`csvsort`、`csvstat`。
> 更多信息：<https://csvkit.readthedocs.io/en/0.9.1/cli.html>。

- 使用自定义分隔符对CSV文件运行命令：

`{{command}} -d {{delimiter}} {{path/to/file.csv}}`

- 使用制表符作为分隔符对CSV文件运行命令（覆盖 -d）：

`{{command}} -t {{path/to/file.csv}}`

- 使用自定义引号字符对CSV文件运行命令：

`{{command}} -q {{quote_char}} {{path/to/file.csv}}`

- 对没有标题行的CSV文件运行命令：

`{{command}} -H {{path/to/file.csv}}`