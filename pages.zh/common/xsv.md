# xsv

> 用 Rust 编写的 CSV 命令行工具包。
> 更多信息：<https://github.com/BurntSushi/xsv>.

- 查看文件的表头：

`xsv headers {{path/to/file.csv}}`

- 统计条目数量：

`xsv count {{path/to/file.csv}}`

- 浏览条目的总体情况：

`xsv stats {{path/to/file.csv}} | xsv table`

- 选择几列：

`xsv select {{column1,column2}} {{path/to/file.csv}}`

- 显示 10 条随机条目：

`xsv sample {{10}} {{path/to/file.csv}}`

- 将一个文件中的列与另一个文件中的列合并：

`xsv join --no-case {{column1}} {{path/to/file1.csv}} {{column2}} {{path/to/file2.csv}} | xsv table`