# head

> 输出文件的第一部分。
> 更多信息：<https://www.gnu.org/software/coreutils/head>。

- 输出文件的前几行：

`head --lines {{count}} {{path/to/file}}`

- 输出文件的前几个字节：

`head --bytes {{count}} {{path/to/file}}`

- 输出文件的所有内容，但不包括最后几行：

`head --lines -{{count}} {{path/to/file}}`

- 输出文件的所有内容，但不包括最后几个字节：

`head --bytes -{{count}} {{path/to/file}}`