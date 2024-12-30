# xsv

> 一个用Rust编写的CSV命令行工具包。
> 更多信息：<https://github.com/BurntSushi/xsv>。

- 检查文件的标题：

`xsv headers {{path/to/file.csv}}`

- 计算条目数量：

`xsv count {{path/to/file.csv}}`

- 获取条目形状的概述：

`xsv stats {{path/to/file.csv}} | xsv table`

- 选择几个列：

`xsv select {{column1,column2}} {{path/to/file.csv}}`

- 显示10个随机条目：

`xsv sample {{10}} {{path/to/file.csv}}`

- 将一个文件中的列连接到另一个文件：

`xsv join --no-case {{column1}} {{path/to/file1.csv}} {{column2}} {{path/to/file2.csv}} | xsv table`