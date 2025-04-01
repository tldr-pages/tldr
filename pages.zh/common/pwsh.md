# pwsh

> 专为系统管理设计的命令行外壳和脚本语言。
> 此命令指 PowerShell 6 及以上版本（也称为 PowerShell Core 和跨平台 PowerShell）。
> 若要使用原始的 Windows 版本（5.1 及以下，也称为旧版 Windows PowerShell），请使用 `powershell` 而不是 `pwsh`。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_pwsh>.

- 启动交互式外壳会话：

`pwsh`

- 启动交互式外壳会话，不加载启动配置文件：

`pwsh -NoProfile`

- 执行特定的命令：

`pwsh -Command "{{echo 'powershell is executed'}}"`

- 执行特定的脚本：

`pwsh -File {{path/to/script.ps1}}`

- 使用特定版本的 PowerShell 启动会话：

`pwsh -Version {{version}}`

- 防止执行启动命令后退出外壳：

`pwsh -NoExit`

- 描述发送到 PowerShell 的数据格式：

`pwsh -InputFormat {{Text|XML}}`

- 确定 PowerShell 输出的格式：

`pwsh -OutputFormat {{Text|XML}}`