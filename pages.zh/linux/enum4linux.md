# enum4linux

> 枚举远程系统上的 Windows 和 Samba 信息。
> 更多信息：<https://labs.portcullis.co.uk/tools/enum4linux/>.

- 尝试使用所有方法枚举：

`enum4linux -a {{remote_host}}`

- 使用给定的登录凭据枚举：

`enum4linux -u {{user_name}} -p {{password}} {{remote_host}}`

- 列出给定主机的用户名：

`enum4linux -U {{remote_host}}`

- 列出共享：

`enum4linux -S {{remote_host}}`

- 获取操作系统信息：

`enum4linux -o {{remote_host}}`
