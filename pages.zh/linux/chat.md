# chat

> 通过调制解调器或串行设备自动处理会话。
> 常用于建立点对点协议（PPP）连接。
> 更多信息：<https://manned.org/chat.8>。

- 从命令行直接执行聊天脚本：

`chat '{{expect_send_pairs}}'`

- 从文件中执行聊天脚本：

`chat -f '{{path/to/chat_script}}'`

- 设置自定义应答等待超时时间（以秒为单位）：

`chat -t {{timeout_in_seconds}} '{{expect_send_pairs}}'`

- 启用详细输出以记录会话到 `syslog`：

`chat -v '{{expect_send_pairs}}'`

- 使用报告文件记录会话中接收到的特定字符串：

`chat -r {{path/to/report_file}} '{{expect_send_pairs}}'`

- 使用变量拨打电话号码，脚本中用 `\T` 替换：

`chat -T '{{phone_number}}' '{{"ATDT\\T CONNECT"}}'`

- 如果接收到特定字符串时，包含一个终止条件：

`chat 'ABORT "{{error_string}}" {{expect_send_pairs}}'`
