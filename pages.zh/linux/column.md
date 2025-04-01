# column

> 将 `stdin` 或文件格式化为多列。
> 列先填满再填行；默认分隔符是空白字符。
> 更多信息：<https://manned.org/column>。

- 将命令的输出格式化为30字符宽的显示：

`printf "header1 header2\nbar foo\n" | column {{[-c|--output-width]}} {{30}}`

- 自动分割列并以表格格式自动对齐：

`printf "header1 header2\nbar foo\n" | column {{[-t|--table]}}`

- 为 `--table` 选项指定列分隔符字符（例如，CSV 文件的分隔符为 ","）（默认为空白字符）：

`printf "header1,header2\nbar,foo\n" | column {{[-t|--table]}} {{[-s|--separator]}} {{,}}`

- 先填行再填列：

`printf "header1\nbar\nfoobar\n" | column {{[-c|--output-width]}} {{30}} {{[-x|--fillrows]}}`