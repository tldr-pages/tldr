# wall

> 在当前登录用户终端上显示一条消息。
> 更多信息：<https://manned.org/wall>.

- 发送一条消息：

`wall {{message}}`

- 向特定用户组发送消息：

`wall {{[-g|--group]}} {{group_name}} {{message}}`

- 从文件发送消息：

`wall {{file}}`

- 以指定超时时间发送消息（默认300秒）：

`wall {{[-t|--timeout]}} {{seconds}} {{file}}`
