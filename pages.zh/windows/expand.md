# 解压

> 解压 Windows Cabinet 文件。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/expand>。

- 将单文件 Cabinet 文件解压到指定目录：

`expand {{path\to\file.cab}} {{path\to\directory}}`

- 显示源 Cabinet 文件中的文件列表：

`expand {{path\to\file.cab}} {{path\to\directory}} -d`

- 从 Cabinet 文件中解压所有文件：

`expand {{path\to\file.cab}} {{path\to\directory}} -f:*`

- 从 Cabinet 文件中解压特定文件：

`expand {{path\to\file.cab}} {{path\to\directory}} -f:{{path\to\file}}`

- 解压时忽略目录结构，并将文件添加到单一目录：

`expand {{path\to\file.cab}} {{path\to\directory}} -i`