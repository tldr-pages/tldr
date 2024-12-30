# cd

> 显示当前工作目录或移动到不同的目录。
> 在 PowerShell 中，此命令是 `Set-Location` 的别名。本文件基于命令提示符（`cmd`）版本的 `cd`。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/cd>。

- 查看等效 PowerShell 命令的文档：

`tldr set-location`

- 显示当前目录的路径：

`cd`

- 前往同一驱动器中的特定目录：

`cd {{path\to\directory}}`

- 前往不同 [d] 驱动器中的特定目录：

`cd /d {{C}}:{{path\to\directory}}`

- 返回当前目录的父目录：

`cd ..`

- 前往当前用户的主目录：

`cd %userprofile%`

- 前往当前驱动器的根目录：

`cd \`