# svcs

> 列出正在运行的服务信息。
> 更多信息：<https://www.unix.com/man-page/linux/1/svcs>.

- 列出所有正在运行的服务：

`svcs`

- 列出未运行的服务：

`svcs -vx`

- 列出特定服务的信息：

`svcs apache`

- 显示服务日志文件的位置：

`svcs -L apache`

- 显示服务日志文件的末尾内容：

`tail $(svcs -L apache)`
