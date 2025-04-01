# mupdf

> 一个轻量级的 PDF、XPS 和电子书查看器。
> 更多信息：<https://www.mupdf.com>.

- 打开 PDF 文件的第一页：

`mupdf {{path/to/file}}`

- 打开 PDF 文件的第 3 页：

`mupdf {{path/to/file}} {{3}}`

- 打开带有密码保护的 PDF 文件：

`mupdf -p {{password}} {{path/to/file}}`

- 以 72 DPI 的初始缩放级别打开 PDF 文件：

`mupdf -r {{72}} {{path/to/file}}`

- 以反色模式打开 PDF 文件：

`mupdf -I {{path/to/file}}`

- 以红色 #FF0000（十六进制颜色代码 RRGGBB）调色的 PDF 文件：

`mupdf -C {{FF0000}}`

- 无抗锯齿（0 = 关闭，8 = 最佳）打开 PDF 文件：

`mupdf -A {{0}}`