# powershell

> 专为系统管理设计的命令行外壳程序和脚本语言。
> 本命令指的是 PowerShell 5.1 及以下版本（也称作旧版 Windows PowerShell）。要使用更新的、跨平台版本的 PowerShell（也称作 PowerShell Core），请使用 `pwsh` 代替 `powershell`。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/powershell>。

- 启动交互式外壳程序会话：

`powershell`

- 启动交互式外壳程序会话而不加载启动配置：

`powershell -NoProfile`

- 执行特定命令：

`powershell -Command "{{echo 'powershell is executed'}}"`

- 执行特定脚本：

`powershell -File {{path/to/script.ps1}}`

- 使用特定版本的 PowerShell 启动会话：

`powershell -Version {{version}}`

- 运行启动命令后防止外壳程序退出：

`powershell -NoExit`

- 描述发送到 PowerShell 的数据格式：

`powershell -InputFormat {{Text|XML}}`

- 确定 PowerShell 输出的格式：

`powershell -OutputFormat {{Text|XML}}`
