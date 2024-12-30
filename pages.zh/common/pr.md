# pr

> 对文件进行分页或列排以便打印。
> 更多信息：<https://www.gnu.org/software/coreutils/pr>。

- 打印多个文件，带有默认的页眉和页脚：

`pr {{path/to/file1 path/to/file2 ...}}`

- 使用自定义居中页眉打印：

`pr -h "{{header}}" {{path/to/file1 path/to/file2 ...}}`

- 打印带有编号行和自定义日期格式：

`pr -n -D "{{format}}" {{path/to/file1 path/to/file2 ...}}`

- 将所有文件一起打印，每列一个，不带页眉或页脚：

`pr -m -T {{path/to/file1 path/to/file2 ...}}`

- 从第2页开始打印到第5页，给定页长（包括页眉和页脚）：

`pr +2:5 -l {{page_length}} {{path/to/file1 path/to/file2 ...}}`

- 打印时，为每行设置偏移量，并截断自定义页宽：

`pr -o {{offset}} -W {{width}} {{path/to/file1 path/to/file2 ...}}`