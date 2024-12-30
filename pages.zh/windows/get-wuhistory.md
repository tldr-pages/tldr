# 获取-WUHistory

> 获取 Windows 更新中已安装更新的历史记录。属于外部 `PSWindowsUpdate` 模块的一部分。
> 此命令只能在 PowerShell 下运行。
> 更多信息：<https://github.com/mgajda83/PSWindowsUpdate>。

- 获取更新历史记录列表：

`Get-WUHistory`

- 列出最近安装的 10 个更新：

`Get-WUHistory -Last {{10}}`

- 列出从特定日期到今天安装的所有更新：

`Get-WUHistory -MaxDate {{date}}`

- 列出过去 24 小时内安装的所有更新：

`Get-WUHistory -MaxDate (Get-Date).AddDays(-1)`

- 通过电子邮件发送结果 (SMTP)：

`Get-WUHistory -SendReport -PSWUSettings @{SmtpServer="{{smtp_server}}"; Port={{smtp_port}} From="{{sender_email}}" To="{{receiver_email}}"}`
