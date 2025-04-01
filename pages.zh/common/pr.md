# pr

> 分页或分列打印文件，以供打印。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/pr-invocation.html>.

- 使用默认的页眉和页脚打印多个文件：

`pr {{path/to/file1 path/to/file2 ...}}`

- 使用自定义居中页眉打印：

`pr {{[-h|--header]}} "{{header}}" {{path/to/file1 path/to/file2 ...}}`

- 打印时添加行号和自定义日期格式：

`pr {{[-n|--number-lines]}} {{[-D|--date-format]}} "{{format}}" {{path/to/file1 path/to/file2 ...}}`

- 一起打印所有文件，每列一个文件，不带页眉或页脚：

`pr {{[-m|--merge]}} {{[-T|--omit-pagination]}} {{path/to/file1 path/to/file2 ...}}`

- 从第2页开始至第5页结束打印，并指定页面长度（包括页眉和页脚）：

`pr +2:5 {{[-l|--length]}} {{page_length}} {{path/to/file1 path/to/file2 ...}}`

- 打印时每行有偏移，并指定自定义页面宽度：

`pr {{[-o|--indent]}} {{offset}} {{[-W|--page_width]}} {{width}} {{path/to/file1 path/to/file2 ...}}`