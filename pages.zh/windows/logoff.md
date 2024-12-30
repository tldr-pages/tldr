# 注销

> 终止登录会话。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/logoff>。

- 终止当前会话：

`logoff`

- 通过会话名称或 ID 终止会话：

`logoff {{session_name|session_id}}`

- 通过 RDP 在特定服务器上终止会话：

`logoff {{session_name|session_id}} /server:{{servername}}`