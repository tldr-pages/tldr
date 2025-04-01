# multitail

> tail 命令的扩展。
> 更多信息：<https://manned.org/multitail>。

- 查看符合模式的所有文件的内容，输出合并为单个流：

`multitail -Q 1 '{{pattern}}'`

- 查看目录中所有文件的内容，输出合并为单个流：

`multitail -Q 1 '{{path/to/directory}}/*'`

- 自动将新文件添加到窗口中：

`multitail -Q {{pattern}}`

- 合并显示5个日志文件，其中2个合并显示，并将它们放置在2列中，左列仅显示1个文件：

`multitail -s 2 -sn 1,3 {{path/to/mergefile}} -I {{path/to/file1}} {{path/to/file2}} {{path/to/file3}} {{path/to/file4}}`
