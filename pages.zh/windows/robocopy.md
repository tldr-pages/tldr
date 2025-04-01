# robocopy

> 强大的文件和文件夹复制工具。
> 默认情况下，只有当源文件和目标文件的时间戳或文件大小不同时，才会复制文件。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/robocopy>。

- 将一个目录中的所有 `.jpg` 和 `.bmp` 文件复制到另一个目录：

`robocopy {{path\to\source_directory}} {{path\to\destination_directory}} {{*.jpg}} {{*.bmp}}`

- 复制所有文件和子目录，包括空目录：

`robocopy {{path\to\source_directory}} {{path\to\destination_directory}} /E`

- 镜像/同步目录，删除目标中不在源中的内容，并复制所有属性和权限：

`robocopy {{path\to\source_directory}} {{path\to\destination_directory}} /MIR /COPYALL`

- 复制所有文件和子目录，但不复制比目标文件旧的源文件：

`robocopy {{path\to\source_directory}} {{path\to\destination_directory}} /E /XO`

- 列出所有 50 MB 或更大的文件，而不是复制它们：

`robocopy {{path\to\source_directory}} {{path\to\destination_directory}} /MIN:{{52428800}} /L`

- 如果网络连接中断允许恢复，并将重试次数限制为 5 次，每次重试等待 15 秒：

`robocopy {{path\to\source_directory}} {{path\to\destination_directory}} /Z /R:5 /W:15`

- 显示帮助：

`robocopy /?`