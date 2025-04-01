# last

> 查看最近登录的用户。
> 更多信息：<https://manned.org/last>.

- 查看从 `/var/log/wtmp` 读取的所有用户的最近登录信息（例如用户名、终端、启动时间、内核）：

`last`

- 列出特定用户的登录信息：

`last {{username}}`

- 指定显示最近登录的次数：

`last {{[-n|--limit]}} {{login_count}}`

- 为条目打印完整日期和时间，然后最后显示主机名列以防止截断：

`last {{[-F|--fulltimes]}} {{[-a|--hostlast]}}`

- 查看特定用户的全部登录记录，并显示IP地址而不是主机名：

`last {{username}} {{[-i|--ip]}}`

- 列出自特定时间以来的信息：

`last {{[-s|--since]}} {{-7days}}`

- 查看所有记录的重启（即伪用户 "reboot" 的最近登录）：

`last reboot`

- 显示帮助：

`last {{[-h|--help]}}`
