# pwsh

> 命令行外壳和脚本语言，专为系统管理设计。
> 此命令指的是 PowerShell 版本 6 及以上（也称为 PowerShell Core 和跨平台 PowerShell）。
> 要使用原始 Windows 版本（5.1 及以下，也称为传统 Windows PowerShell），请使用 `powershell` 而不是 `pwsh`。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_pwsh>。

- 启动一个交互式 shell 会话：

`pwsh`

- 启动一个不加载启动配置的交互式 shell 会话：

`pwsh -NoProfile`

- 执行特定命令：

`pwsh -Command "{{echo 'powershell is executed'}}"`

- 执行特定脚本：

`pwsh -File {{path/to/script.ps1}}`

- 启动一个特定版本的 PowerShell 会话：

`pwsh -Version {{version}}`

- 防止 shell 在执行启动命令后退出：

`pwsh -NoExit`

- 描述发送到 PowerShell 的数据格式：

`pwsh -InputFormat {{Text|XML}}`

- 确定 PowerShell 输出的格式：

`pwsh -OutputFormat {{Text|XML}}`