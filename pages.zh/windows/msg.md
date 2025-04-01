# msg

> 向指定的用户或会话发送信息。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/msg>.

- 向指定的用户或会话发送信息：

`msg {{用户名|会话名|会话 id}} {{信息}}`

- 从标准输入发送信息：

`echo "{{信息}}" | msg {{用户名|会话名|会话 id}}`

- 向指定的服务器发送消息：

`msg /server:{{服务器名称}} {{用户名|会话名|会话 id}}`

- 向当前计算机的所有用户发送消息：

`msg *`

- 设置发送消息的延迟：

`msg /time:{{秒}}`
