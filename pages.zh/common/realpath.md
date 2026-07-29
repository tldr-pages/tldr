# realpath

> 显示文件或目录的解析后绝对路径。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/realpath-invocation.html>。

- 显示文件或目录的绝对路径：

`realpath {{路径/到/文件或目录}}`

- 要求所有路径组件都必须存在：

`realpath {{[-e|--canonicalize-existing]}} {{路径/到/文件或目录}}`

- 在符号链接之前解析 `..` 组件：

`realpath {{[-L|--logical]}} {{路径/到/文件或目录}}`

- 禁用符号链接展开：

`realpath {{[-s|--no-symlinks]}} {{路径/到/文件或目录}}`

- 抑制错误消息：

`realpath {{[-q|--quiet]}} {{路径/到/文件或目录}}`
