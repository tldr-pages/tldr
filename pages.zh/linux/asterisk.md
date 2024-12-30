# Asterisk

> 运行和管理电话和交换（电话）服务器实例。
> 更多信息：<https://docs.asterisk.org>。

- [R] 重新连接到正在运行的服务器，并打开 3 级 [v] 详细日志：

`asterisk -r -vvv`

- [R] 重新连接到正在运行的服务器，运行一个命令并返回：

`asterisk -r -x "{{command}}"`

- 显示 chan_SIP 客户端（电话）：

`asterisk -r -x "sip show peers"`

- 显示活动通话和通道：

`asterisk -r -x "core show channels"`

- 显示语音邮件邮箱：

`asterisk -r -x "voicemail show users"`

- 终止一个通道：

`asterisk -r -x "hangup request {{channel_ID}}"`

- 重新加载 chan_SIP 配置：

`asterisk -r -x "sip reload"`