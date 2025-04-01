# query

> 显示关于用户会话和进程的信息。
> 更多信息: <https://learn.microsoft.com/windows-server/administration/windows-commands/query>.

- 显示所有用户会话:

`query session`

- 显示远程计算机上的当前用户会话:

`query session /server:{{hostname}}`

- 显示已登录的用户:

`query user`

- 显示远程计算机上的所有用户会话:

`query session /server:{{hostname}}`

- 显示所有运行中的进程:

`query process`

- 按会话或用户名显示运行中的进程:

`query process {{session_name|user_name}}`