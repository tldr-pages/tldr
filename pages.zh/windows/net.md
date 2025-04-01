# net

> 系统工具，用于查看和修改与网络相关的设置。
> 更多信息：<https://learn.microsoft.com/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/gg651155(v=ws.11)>.

- 同步启动或停止 Windows 服务：

`net {{start|stop}} {{service}}`

- 确保当前控制台中可用的 SMB 共享：

`net use {{\\smb_shared_folder}} /USER:{{username}}`

- 显示当前通过 SMB 共享的文件夹：

`net share`

- 显示正在使用你的 SMB 共享的用户（在提升的控制台中运行）：

`net session`

- 显示本地安全组中的用户：

`net localgroup "{{Administrators}}"`

- 将用户添加到本地安全组（在提升的控制台中运行）：

`net localgroup "{{Administrators}}" {{username}} /add`

- 显示子命令的帮助：

`net help {{subcommand}}`

- 显示帮助：

`net help`