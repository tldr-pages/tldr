# Get-WUHistory

> 获取 Windows Update 安装的更新历史记录。此命令属于外部 `PSWindowsUpdate` 模块。
> 该命令只能在 PowerShell 下运行。
> 更多信息：<https://github.com/mgajda83/PSWindowsUpdate>.

- 获取更新历史记录列表：

`Get-WUHistory`

- 列出最后 10 次安装的更新：

`Get-WUHistory -Last {{10}}`

- 列出从特定日期到今天的安装的所有更新：

`Get-WUHistory -MaxDate {{date}}`

- 列出过去 24 小时内安装的所有更新：

`Get-WUHistory -MaxDate (Get-Date).AddDays(-1)`

- 通过电子邮件（SMTP）发送结果：

`Get-WUHistory -SendReport -PSWUSettings @{SmtpServer="{{smtp_server}}"; Port={{smtp_port}} From="{{sender_email}}" To="{{receiver_email}}"}`