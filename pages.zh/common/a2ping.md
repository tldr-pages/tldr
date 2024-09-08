# a2ping

> 将图像转换为 EPS 或 PDF 文件。
> 更多信息：<https://manned.org/a2ping>.

- 将图像转换为 PDF（注意：指定输出文件名是可选的）：

`a2ping {{图像文件}} {{输出PDF文件}}`

- 使用指定的方法压缩文档：

`a2ping --nocompress {{none|zip|best|flate}} {{文件}}`

- 如果存在，则扫描 HiResBoundingBox（默认为是）：

`a2ping --nohires {{文件}}`

- 允许页面内容位于原点的下方和左侧（默认为否）：

`a2ping --below {{文件}}`

- 将额外的参数传递给 `gs`：

`a2ping --gsextra {{参数}} {{文件}}`

- 将额外的参数传递给外部程序（如 `pdftops`）：

`a2ping --extra {{参数}} {{文件}}`

- 显示帮助信息：

`a2ping -h`
