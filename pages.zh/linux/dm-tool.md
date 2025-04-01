# dm-tool

> 与显示管理器通信的工具。
> 更多信息：<https://manned.org/dm-tool>.

- 显示登录界面，同时保持当前桌面会话打开，并在登录用户认证后恢复：

`dm-tool switch-to-greeter`

- 锁定当前会话：

`dm-tool lock`

- 切换到特定用户，如果需要则显示认证提示：

`dm-tool switch-to-user {{username}} {{session}}`

- 在运行中的 LightDM 会话中添加一个动态席位：

`dm-tool add-seat {{xlocal}} {{name}}={{value}}`