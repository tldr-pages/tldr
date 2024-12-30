# robocopy

> 强大的文件和文件夹复制工具。
> 默认情况下，仅在源和目标的时间戳或文件大小不同的情况下才会复制文件。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/robocopy>。

- 从一个目录复制所有 `.jpg` 和 `.bmp` 文件到另一个目录：

`robocopy {{path\to\source_directory}} {{path\to\destination_directory}} {{*.jpg}} {{*.bmp}}`

- 复制所有文件和子目录，包括空的子目录：

`robocopy {{path\to\source_directory}} {{path\to\destination_directory}} /E`

- 镜像/同步一个目录，删除源中没有的任何内容，并包含所有属性和权限：

`robocopy {{path\to\source_directory}} {{path\to\destination_directory}} /MIR /COPYALL`

- 复制所有文件和子目录，排除比目标文件更旧的源文件：

`robocopy {{path\to\source_directory}} {{path\to\destination_directory}} /E /XO`

- 列出所有大小为 50 MB 或更大的文件，而不进行复制：

`robocopy {{path\to\source_directory}} {{path\to\destination_directory}} /MIN:{{52428800}} /L`

- 如果网络连接丢失，允许恢复，并将重试次数限制为 5 次，等待时间为 15 秒：

`robocopy {{path\to\source_directory}} {{path\to\destination_directory}} /Z /R:5 /W:15`

- 显示帮助信息：

`robocopy /?`