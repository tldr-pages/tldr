# 移动

> 移动或重命名文件和目录。
> 在 PowerShell 中，此命令是 `Move-Item` 的别名。此文档基于命令提示符（`cmd`）版本的 `move`。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/move>。

- 查看等效 PowerShell 命令的文档：

`tldr move-item`

- 在目标不是现有目录时重命名文件或目录：

`move {{path\to\source}} {{path\to\target}}`

- 将文件或目录移动到现有目录中：

`move {{path\to\source}} {{path\to\existing_directory}}`

- 跨驱动器移动文件或目录：

`move {{C:\path\to\source}} {{D:\path\to\target}}`

- 在覆盖现有文件之前不提示确认：

`move /Y {{path\to\source}} {{path\to\existing_directory}}`

- 在覆盖现有文件之前提示确认，无论文件权限如何：

`move /-Y {{path\to\source}} {{path\to\existing_directory}}`