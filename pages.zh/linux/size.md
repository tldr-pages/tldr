# size

> 显示二进制文件中各个部分的大小。
> 更多信息：<https://sourceware.org/binutils/docs/binutils/size.html>。

- 显示给定目标文件或可执行文件中各部分的大小：

`size {{path/to/file}}`

- 以 [o]ctal 形式显示给定目标文件或可执行文件中各部分的大小：

`size {{-o|--radix=8}} {{path/to/file}}`

- 以 [d]ecimal 形式显示给定目标文件或可执行文件中各部分的大小：

`size {{-d|--radix=10}} {{path/to/file}}`

- 以 he[x]adecimal 形式显示给定目标文件或可执行文件中各部分的大小：

`size {{-x|--radix=16}} {{path/to/file}}`