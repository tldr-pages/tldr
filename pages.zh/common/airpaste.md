# airpaste

> 使用 mDNS 在同一网络上共享消息和文件。
> 更多信息：<https://github.com/mafintosh/airpaste>。

- 等待消息并在接收到时显示：

`airpaste`

- 发送文本：

`echo {{文本}} | airpaste`

- 发送文件：

`airpaste < {{文件路径}}`

- 接收文件：

`airpaste > {{文件路径}}`

- 创建或加入频道：

`airpaste {{频道名称}}`