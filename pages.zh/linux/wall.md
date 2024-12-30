# wall

> 在当前登录的用户终端上写消息。
> 更多信息：<https://manned.org/wall>。

- 发送消息：

`wall {{message}}`

- 向属于特定组的用户发送消息：

`wall --group {{group_name}} {{message}}`

- 从文件发送消息：

`wall {{file}}`

- 发送带超时的消息（默认300秒）：

`wall --timeout {{seconds}} {{file}}`