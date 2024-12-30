# last

> 查看最后登录的用户。
> 更多信息: <https://manned.org/last>。

- 查看最后的登录情况、其持续时间以及从 `/var/log/wtmp` 读取的其他信息：

`last`

- 指定要显示的最后登录次数：

`last -n {{login_count}}`

- 打印条目的完整日期和时间，然后将主机名列最后显示以防止截断：

`last -F -a`

- 查看特定用户的所有登录记录，并显示IP地址而不是主机名：

`last {{username}} -i`

- 查看所有记录的重启（即伪用户“reboot”的最后登录）：

`last reboot`

- 查看所有记录的关机（即伪用户“shutdown”的最后登录）：

`last shutdown`