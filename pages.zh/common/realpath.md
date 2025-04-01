# realpath

> 显示文件或目录的解析后的绝对路径。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/realpath-invocation.html>.

- 显示文件或目录的绝对路径：

`realpath {{path/to/file_or_directory}}`

- 要求所有路径组件都存在：

`realpath {{[-e|--canonicalize-existing]}} {{path/to/file_or_directory}}`

- 在解析符号链接之前解析 ".." 组件：

`realpath {{[-L|--logical]}} {{path/to/file_or_directory}}`

- 禁用符号链接的展开：

`realpath {{[-s|--no-symlinks]}} {{path/to/file_or_directory}}`

- 抑制错误信息：

`realpath {{[-q|--quiet]}} {{path/to/file_or_directory}}`
