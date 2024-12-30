# ncdu

> 带有 ncurses 界面的磁盘使用分析器。
> 更多信息：<https://manned.org/ncdu>。

- 分析当前工作目录：

`ncdu`

- 彩色输出：

`ncdu --color {{dark|off}}`

- 分析指定目录：

`ncdu {{path/to/directory}}`

- 将结果保存到文件：

`ncdu -o {{path/to/file}}`

- 排除与模式匹配的文件，可以多次给出参数以添加更多模式：

`ncdu --exclude '{{*.txt}}'`