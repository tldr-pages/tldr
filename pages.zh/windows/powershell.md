# PowerShell

> 命令行外壳和脚本语言，专为系统管理而设计。
> 此命令指的是 PowerShell 版本 5.1 及以下（也称为传统 Windows PowerShell）。要使用更新的跨平台版本 PowerShell（也称为 PowerShell Core），请使用 `pwsh` 而不是 `powershell`。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/powershell>。

- 启动一个交互式外壳会话：

`powershell`

- 启动一个不加载启动配置的交互式外壳会话：

`powershell -NoProfile`

- 执行特定命令：

`powershell -Command "{{echo 'powershell is executed'}}"`

- 执行特定脚本：

`powershell -File {{path/to/script.ps1}}`

- 启动一个特定版本的 PowerShell 会话：

`powershell -Version {{version}}`

- 防止外壳在运行启动命令后退出：

`powershell -NoExit`

- 描述发送到 PowerShell 的数据格式：

`powershell -InputFormat {{Text|XML}}`

- 确定 PowerShell 输出的格式：

`powershell -OutputFormat {{Text|XML}}`