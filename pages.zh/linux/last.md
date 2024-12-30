# last

> 列出最后用户登录的信息。
> 另见: `lastb`, `login`。
> 更多信息: <https://manned.org/last.1>。

- 列出所有用户的登录信息（例如，用户名、终端、启动时间、内核）：

`last`

- 列出特定用户的登录信息：

`last {{username}}`

- 列出特定TTY的信息：

`last {{tty1}}`

- 列出最近的信息（默认情况下，最新的在最上面）：

`last | tac`

- 列出系统启动的信息：

`last "{{system boot}}"`

- 列出特定[t]imestamp格式的信息：

`last --time-format {{notime|full|iso}}`

- 列出自特定时间和日期[s]ince以来的信息：

`last --since {{-7days}}`

- 列出远程主机的信息（即主机名和IP）：

`last --dns`