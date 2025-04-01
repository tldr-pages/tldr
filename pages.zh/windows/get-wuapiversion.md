# Get-WUApiVersion

> 获取 Windows Update Agent 的版本。属于外部 `PSWindowsUpdate` 模块。
> 此命令只能在 PowerShell 下运行。
> 更多信息：<https://github.com/mgajda83/PSWindowsUpdate>.

- 获取当前安装的 Windows Update Agent 版本：

`Get-WUApiVersion`

- 通过电子邮件（SMTP）发送当前配置数据：

`Get-WUApiVersion -SendReport -PSWUSettings @{SmtpServer="{{smtp_server}}"; Port={{smtp_port}} From="{{sender_email}}" To="{{receiver_email}}"}`
