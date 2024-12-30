# enca

> 检测和转换文本文件的编码。
> 更多信息：<https://github.com/nijel/enca>。

- 根据系统的区域设置检测文件编码：

`enca {{path/to/file1 path/to/file2 ...}}`

- 指定POSIX/C区域格式的语言（例如zh_CN，en_US）检测文件编码：

`enca -L {{language}} {{path/to/file1 path/to/file2 ...}}`

- 将文件转换为特定编码：

`enca -L {{language}} -x {{to_encoding}} {{path/to/file1 path/to/file2 ...}}`

- 使用不同的编码创建现有文件的副本：

`enca -L {{language}} -x {{to_encoding}} < {{original_file}} > {{new_file}}`