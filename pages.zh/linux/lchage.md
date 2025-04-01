# lchage

> 显示或更改用户密码策略。
> 更多信息：<https://manned.org/lchage>.

- 为用户禁用密码过期：

`sudo lchage --date -1 {{username}}`

- 显示用户的密码策略：

`sudo lchage --list {{username}}`

- 在用户上次更改密码后的指定天数后要求用户更改密码：

`sudo lchage --maxdays {{number_of_days}} {{username}}`

- 在密码过期前的指定天数开始警告用户：

`sudo lchage --warndays {{number_of_days}} {{username}}`
