# 消息

> 向用户或会话发送消息。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/msg>。

- 向指定用户或会话发送消息：

`msg {{用户名|会话名称|会话ID}} {{消息}}`

- 从 `stdin` 发送消息：

`echo "{{消息}}" | msg {{用户名|会话名称|会话ID}}`

- 向特定服务器发送消息：

`msg /server:{{服务器名称}} {{用户名|会话名称|会话ID}}`

- 向当前计算机的所有用户发送消息：

`msg *`

- 设置消息延迟（以秒为单位）：

`msg /time:{{10}}`