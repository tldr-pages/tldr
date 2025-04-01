# cd

> 显示当前工作目录或切换到其他目录。
> 在 PowerShell 中，此命令是 `Set-Location` 的别名。此文档基于命令提示符 (`cmd`) 版本的 `cd`。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/cd>。

- 查看等效的 PowerShell 命令的文档：

`tldr set-location`

- 显示当前目录的路径：

`cd`

- 切换到同一磁盘的特定目录：

`cd {{path\to\directory}}`

- 切换到不同磁盘的特定目录：

`cd /d {{C}}:{{path\to\directory}}`

- 切换到当前目录的上级目录：

`cd ..`

- 切换到当前用户的主目录：

`cd %userprofile%`

- 切换到当前磁盘的根目录：

`cd \`
