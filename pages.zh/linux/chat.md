# chat

> 自动化与调制解调器或串行设备的对话。
> 常用于建立 PPP（点对点协议）连接。
> 更多信息：<https://manned.org/chat.8>。

- 从命令行直接执行聊天脚本：

`chat '{{expect_send_pairs}}'`

- 从文件中执行聊天脚本：

`chat -f '{{path/to/chat_script}}'`

- 设置自定义超时时间（以秒为单位）以期待响应：

`chat -t {{timeout_in_seconds}} '{{expect_send_pairs}}'`

- 启用详细输出以将对话记录到 `syslog`：

`chat -v '{{expect_send_pairs}}'`

- 使用报告文件记录在对话中收到的特定字符串：

`chat -r {{path/to/report_file}} '{{expect_send_pairs}}'`

- 使用变量拨打电话号码，在脚本中替换 `\T`：

`chat -T '{{phone_number}}' '{{"ATDT\\T CONNECT"}}'`

- 包含一个中止条件，如果收到特定字符串：

`chat 'ABORT "{{error_string}}" {{expect_send_pairs}}'`