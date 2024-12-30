# basename

> 从路径中移除前导目录部分。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/basename-invocation.html>。

- 仅显示路径中的文件名：

`basename {{path/to/file}}`

- 仅显示路径中最右侧的目录名：

`basename {{path/to/directory}}`

- 仅显示路径中的文件名，并移除后缀：

`basename {{path/to/file}} {{suffix}}`