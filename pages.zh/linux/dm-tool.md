# dm-tool

> 用于与显示管理器通信的工具。
> 更多信息：<https://manned.org/dm-tool>。

- 在保持当前桌面会话打开并等待已登录用户身份验证后恢复的情况下显示问候者：

`dm-tool switch-to-greeter`

- 锁定当前会话：

`dm-tool lock`

- 切换到特定用户，如有必要显示身份验证提示：

`dm-tool switch-to-user {{username}} {{session}}`

- 在运行的 LightDM 会话中添加动态座席：

`dm-tool add-seat {{xlocal}} {{name}}={{value}}`