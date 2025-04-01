# faillock

> 显示和修改身份验证失败记录文件。
> 更多信息：<https://manned.org/faillock>.

- 列出当前用户的登录失败记录：

`faillock`

- 重置当前用户的失败记录：

`faillock --reset`

- 列出所有用户的登录失败记录：

`sudo faillock`

- 列出指定用户的登录失败记录：

`sudo faillock --user {{user}}`

- 重置指定用户的失败记录：

`sudo faillock --user {{user}} --reset`