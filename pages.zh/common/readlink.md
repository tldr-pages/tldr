# readlink

> 跟踪符号链接并获取符号链接信息。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/readlink-invocation.html>。

- 获取符号链接指向的实际文件：

`readlink {{path/to/file}}`

- 获取文件的绝对路径：

`readlink {{[-f|--canonicalize]}} {{path/to/file}}`
