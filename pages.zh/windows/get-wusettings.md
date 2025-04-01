# Get-WUSettings

> 获取当前的 Windows 更新代理配置。属于外部 `PSWindowsUpdate` 模块。
> 该命令只能在 PowerShell 下运行。
> 更多信息：<https://github.com/mgajda83/PSWindowsUpdate>.

- 获取当前的 Windows 更新代理配置：

`Get-WUSettings`

- 通过电子邮件（SMTP）发送当前配置数据：

`Get-WUSettings -SendReport -PSWUSettings @{SmtpServer="{{smtp_server}}"; Port={{smtp_port}}; From="{{sender_email}}"; To="{{receiver_email}}"}`