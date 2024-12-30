# multitail

> tail 的扩展。
> 更多信息：<https://manned.org/multitail>。

- 在单个流中监视所有匹配模式的文件：

`multitail -Q 1 '{{pattern}}'`

- 在单个流中监视目录中的所有文件：

`multitail -Q 1 '{{path/to/directory}}/*'`

- 自动将新文件添加到窗口：

`multitail -Q {{pattern}}`

- 显示 5 个日志文件，同时合并 2 个，并将它们放在 2 列中，左列仅显示一个：

`multitail -s 2 -sn 1,3 {{path/to/mergefile}} -I {{path/to/file1}} {{path/to/file2}} {{path/to/file3}} {{path/to/file4}}`