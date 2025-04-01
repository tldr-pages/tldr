# pdbedit

> 编辑 Samba 用户数据库。
> 对于简单的用户添加、删除或密码修改，您也可以使用 `smbpasswd`。
> 更多信息：<https://manned.org/pdbedit>。

- 列出所有 Samba 用户（使用详细标志显示其设置）：

`sudo pdbedit --list --verbose`

- 将现有的 Unix 用户添加到 Samba（将提示输入密码）：

`sudo pdbedit --user {{username}} --create`

- 删除 Samba 用户：

`sudo pdbedit --user {{username}} --delete`

- 重置 Samba 用户的失败密码计数器：

`sudo pdbedit --user {{username}} --bad-password-count-reset`
