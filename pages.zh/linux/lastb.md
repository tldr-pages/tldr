# lastb

> 列出最近登录的用户。
> 更多信息：<https://manned.org/lastb>.

- 列出最近登录的用户：

`sudo lastb`

- 列出自某个时间以来所有最近登录的用户：

`sudo lastb {{[-s|--since]}} {{YYYY-MM-DD}}`

- 列出截至某个时间为止所有最近登录的用户：

`sudo lastb {{[-t|--until]}} {{YYYY-MM-DD}}`

- 列出在特定时间登录的所有用户：

`sudo lastb {{[-p|--present]}} {{hh:mm}}`

- 列出所有最近登录的用户，并将 IP 地址转换为主机名：

`sudo lastb {{[-d|--dns]}}`
