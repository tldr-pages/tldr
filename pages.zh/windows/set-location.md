# Set-Location

> 显示当前工作目录或移动到不同的目录。
> 注意：此命令只能在 PowerShell 中使用。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.management/set-location>.

- 转到指定的目录：

`Set-Location {{path\to\directory}}`

- 转到不同驱动器中的特定目录：

`Set-Location {{C}}:{{path\to\directory}}`

- 转到并显示指定目录的位置：

`Set-Location {{path\to\directory}} -PassThru`

- 返回到当前目录的父目录：

`Set-Location ..`

- 转到当前用户的主目录：

`Set-Location ~`

- 返回/前进到之前选择的目录：

`Set-Location {{-|+}}`

- 转到当前驱动器的根目录：

`Set-Location \`