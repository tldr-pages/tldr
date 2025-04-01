# ncdu

> 带有 ncurses 界面的磁盘使用情况分析器。
> 更多信息：<https://manned.org/ncdu>.

- 分析当前工作目录：

`ncdu`

- 使用颜色显示输出：

`ncdu --color {{dark|off}}`

- 分析指定目录：

`ncdu {{path/to/directory}}`

- 将结果保存到文件：

`ncdu -o {{path/to/file}}`

- 排除符合模式的文件，可以多次使用此参数以添加更多模式：

`ncdu --exclude '{{*.txt}}'`
