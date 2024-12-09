# pr

> 对文件进行分页或分栏以便打印。
> 更多信息：<https://www.gnu.org/software/coreutils/pr>。

- 使用默认页眉和页脚打印多个文件：

`pr {{路径/到/文件1 路径/到/文件2 ...}}`

- 使用自定义居中标题打印：
`pr -h "{{header}}" {{path/to/file1 path/to/file2 ...}}`

- 使用编号行和自定义日期格式打印：

`pr -n -D "{{format}}" {{path/to/file1 path/to/file2 ...}}`

- 一起打印所有文件，每列一个，不带页眉或页脚：

`pr -m -T {{路径/到/文件1 路径/到/文件2 ...}}`

- 打印，从第 2 页开始到第 5 页，具有给定的页面长度（包括页眉和页脚）：

`pr +2:5 -l {{page_length}} {{路径/到/文件1 路径/到/文件2 ...}}`

- 使用每行的偏移量和截断的自定义页面宽度进行打印：

`pr -o {{offset}} -W {{width}} {{path/to/file1 path/to/file2 ...}}`

