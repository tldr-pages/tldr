# mupdf

> 一个轻量级的 PDF、XPS 和电子书查看器。
> 更多信息：<https://www.mupdf.com>。

- 在第一页打开 PDF：

`mupdf {{path/to/file}}`

- 在第 3 页打开 PDF：

`mupdf {{path/to/file}} {{3}}`

- 打开一个受密码保护的 PDF：

`mupdf -p {{password}} {{path/to/file}}`

- 以初始缩放级别（以 DPI 表示）为 72 打开 PDF：

`mupdf -r {{72}} {{path/to/file}}`

- 以反色方式打开 PDF：

`mupdf -I {{path/to/file}}`

- 以红色 #FF0000（十六进制颜色语法 RRGGBB）打开 PDF：

`mupdf -C {{FF0000}}`

- 以无抗锯齿效果打开 PDF（0 = 关闭，8 = 最佳）：

`mupdf -A {{0}}`