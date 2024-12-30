# lchage

> 显示或更改用户密码策略。
> 更多信息请访问：<https://manned.org/lchage>。

- 禁用用户的密码过期：

`sudo lchage --date -1 {{用户名}}`

- 显示用户的密码策略：

`sudo lchage --list {{用户名}}`

- 要求用户在上次密码更改后的某个天数内更改密码：

`sudo lchage --maxdays {{天数}} {{用户名}}`

- 在密码过期前的某个天数开始警告用户：

`sudo lchage --warndays {{天数}} {{用户名}}`