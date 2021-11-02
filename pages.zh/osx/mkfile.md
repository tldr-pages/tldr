# mkfile

> 创建一个或多个任意大小的空文件。
> 更多信息：<https://ss64.com/osx/mkfile.html>.

- 创建一个 15 千字节的空文件：

`mkfile -n {{15k}} {{文件名}}`

- 创建给定大小和单位的文件（bytes, KB, MB, GB）：

`mkfile -n {{大小}}{{b|k|m|g}} {{文件名}}`

- 创建两个 4 兆字节的文件：

`mkfile -n {{4m}} {{文件名 1}} {{文件名 2}}`
