# ncdu

> 带 ncurses 界面的磁盘占用分析器。
> 另请参阅：`duf`, `df`。
> 更多信息：<https://dev.yorhel.nl/ncdu/man>。

- 分析当前工作目录：

`ncdu`

- 输出着色：

`ncdu --color {{dark|off}}`

- 分析指定目录：

`ncdu {{路径/到/目录}}`

- 将结果保存到文件：

`ncdu -o {{路径/到/文件}}`

- 排除符合某个条件的文件，可多次指定以添加更多条件：

`ncdu --exclude '{{*.txt}}'`
