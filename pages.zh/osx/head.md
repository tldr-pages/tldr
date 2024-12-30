# head

> 输出文件的第一部分。
> 更多信息：<https://keith.github.io/xcode-man-pages/head.1.html>。

- 输出文件的前几行：

`head --lines {{8}} {{path/to/file}}`

- 输出文件的前几个字节：

`head --bytes {{8}} {{path/to/file}}`

- 输出文件的所有内容，除了最后几行：

`head --lines -{{8}} {{path/to/file}}`

- 输出文件的所有内容，除了最后几个字节：

`head --bytes -{{8}} {{path/to/file}}`