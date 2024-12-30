# a2ping

> 将图像转换为 EPS 或 PDF 文件。
> 更多信息：<https://manned.org/a2ping>。

- 将图像转换为 PDF（注意：指定输出文件名是可选的）：

`a2ping {{path/to/image.ext}} {{path/to/output.pdf}}`

- 使用指定的方法压缩文档：

`a2ping --nocompress {{none|zip|best|flate}} {{path/to/file}}`

- 如果存在，扫描 HiResBoundingBox（默认为是）：

`a2ping --nohires {{path/to/file}}`

- 允许页面内容位于原点下方和左侧（默认为否）：

`a2ping --below {{path/to/file}}`

- 传递额外参数给 `gs`：

`a2ping --gsextra {{arguments}} {{path/to/file}}`

- 传递额外参数给外部程序（即 `pdftops`）：

`a2ping --extra {{arguments}} {{path/to/file}}`

- 显示帮助信息：

`a2ping -h`