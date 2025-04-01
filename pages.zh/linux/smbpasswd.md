# smbpasswd

> 添加/删除 Samba 用户或更改其密码。
> Samba 用户必须有一个已存在的本地 Unix 账户。
> 更多信息：<https://manned.org/smbpasswd.8>.

- 更改当前用户的 SMB 密码：

`smbpasswd`

- 添加指定的用户到 Samba 并设置密码（用户应已存在于系统中）：

`sudo smbpasswd -a {{username}}`

- 修改已存在的 Samba 用户的密码：

`sudo smbpasswd {{username}}`

- 删除 Samba 用户（如果 Unix 账户已被删除，请使用 `pdbedit`）：

`sudo smbpasswd -x {{username}}`