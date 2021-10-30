# powershell

> 专为系统管理而设计的命令行 shell 和脚本语言。
> 更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/powershell>.

- 在命令提示符窗口中启动 Windows PowerShell 会话：

`powershell`

- 加载一个特定的 PowerShell 控制台文件：

`powershell -PSConsoleFile {{路径/file}}`

- 用指定版本的 PowerShell 启动会话：

`powershell -Version {{版本}}`

- 防止运行启动命令后 shell 退出：

`powershell -NoExit`

- 描述发送到 PowerShell 的数据格式：

`powershell -InputFormat {{Text|XML}}`

- 设定 PowerShell 输出的格式：

`powershell -OutputFormat {{Text|XML}}`

- 显示帮助：

`powershell -Help`
