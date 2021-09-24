# chage

> 更改用户账户和密码到期信息。
> 更多信息：<https://manned.org/chage>.

- 列出用户的密码信息：

`chage --list {{用户名}}`

- 启用密码在 10 天内过期：

`sudo chage --maxdays {{10}} {{用户名}}`

- 关闭密码过期：

`sudo chage --maxdays {{-1}} {{用户名}}`

- 设置账户到期日期：

`sudo chage --expiredate {{YYYY-MM-DD}} {{用户名}}`

- 强制用户在下次登录时更改密码：

`sudo chage --lastday {{0}} {{用户名}}`
