# expand

> 解压一个或多个 cab 文件。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/expand>.

- 将单文件 cab 文件解压到指定目录：

`expand {{cab 文件路径}} {{指定的目录}}`

- 列出 cab 文件中的所有文件：

`expand {{cab 文件路径}} {{指定的目录}} -d`

- 从 cab 文件中解压所有的文件：

`expand {{cab 文件路径}} {{指定的目录}} -f:*`

- 从 cab 文件中解压一个特定的文件：

`expand {{cab 文件路径}} {{指定的目录}} -f:{{文件名}}`

- 解压缩时忽略目录结构，并将它们添加到单个目录中：

`expand {{cab 文件路径}} {{指定的目录}} -i`
