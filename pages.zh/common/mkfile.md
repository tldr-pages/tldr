# mkfile

> 创建任意大小的空文件。
> 更多信息：<https://manned.org/mkfile>。

- 创建一个15千字节的空文件：

`mkfile -n {{15k}} {{path/to/file}}`

- 创建一个指定大小和单位（字节、千字节、兆字节、吉字节）的文件：

`mkfile -n {{size}}{{b|k|m|g}} {{path/to/file}}`

- 创建两个各为4兆字节的文件：

`mkfile -n {{4m}} {{first_filename}} {{second_filename}}`