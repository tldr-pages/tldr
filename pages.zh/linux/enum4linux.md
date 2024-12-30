# enum4linux

> 从远程系统枚举Windows和Samba信息。
> 更多信息请访问：<https://labs.portcullis.co.uk/tools/enum4linux/>。

- 尝试使用所有方法进行枚举：

`enum4linux -a {{remote_host}}`

- 使用给定的登录凭据进行枚举：

`enum4linux -u {{user_name}} -p {{password}} {{remote_host}}`

- 从给定主机列出用户名：

`enum4linux -U {{remote_host}}`

- 列出共享：

`enum4linux -S {{remote_host}}`

- 获取操作系统信息：

`enum4linux -o {{remote_host}}`