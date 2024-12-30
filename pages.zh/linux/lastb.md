# lastb

> 列出最近登录的用户。
> 更多信息：<https://manned.org/lastb>。

- 列出最近登录的用户：

`sudo lastb`

- 列出自给定时间以来的所有最近登录的用户：

`sudo lastb --since {{YYYY-MM-DD}}`

- 列出直到给定时间的所有最近登录的用户：

`sudo lastb --until {{YYYY-MM-DD}}`

- 列出特定时间登录的所有用户：

`sudo lastb --present {{hh:mm}}`

- 列出所有最近登录的用户并将IP转换为主机名：

`sudo lastb --dns`