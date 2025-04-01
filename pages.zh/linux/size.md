# size

> 显示二进制文件中各节的大小。
> 更多信息：<https://sourceware.org/binutils/docs/binutils/size.html>。

- 显示指定对象文件或可执行文件中各节的大小：

`size {{path/to/file}}`

- 使用八进制显示指定对象文件或可执行文件中各节的大小：

`size {{[-o|--radix=8]}} {{path/to/file}}`

- 使用十进制显示指定对象文件或可执行文件中各节的大小：

`size {{[-d|--radix=10]}} {{path/to/file}}`

- 使用十六进制显示指定对象文件或可执行文件中各节的大小：

`size {{[-x|--radix=16]}} {{path/to/file}}`
