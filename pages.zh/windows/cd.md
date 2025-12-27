# cd

> 显示当前工作目录或移动到其他工作目录。
> 在 PowerShell 中，此命令是“Set-Location”的别名。本文档基于的是命令提示符（cmd）版本的 。
> 更多信息：[https://learn.microsoft.com/windows-server/administration/windows-commands/cd.]

- 原命令的文档在：

`tldr set-location`

- 显示当前目录的路径

`cd`

- 访问当前硬盘的某一个特定目录

`cd {{path\to\directory}}`

- 转到位于另一驱动器上的特定目录：

`cd /d {{C}}:{{path\to\directory}}`

- 访问当前目录的上级目录：

`cd ..`

- 访问当前用户的主目录：

`cd %userprofile%`

- 访问当前驱动器的根目录：

`cd \`
