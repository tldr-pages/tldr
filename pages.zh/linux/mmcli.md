# mmcli

> 控制和监控 ModemManager。
> 更多信息：<https://www.freedesktop.org/software/ModemManager/man/latest/mmcli.1.html>.

- 列出可用的调制解调器：

`mmcli --list-modems`

- 打印调制解调器的信息：

`mmcli --modem={{modem}}`

- 启用调制解调器：

`mmcli --modem={{modem}} --enable`

- 列出调制解调器上的可用 SMS 消息：

`sudo mmcli --modem={{modem}} --messaging-list-sms`

- 从调制解调器中删除指定路径的消息：

`sudo mmcli --modem={{modem}} --messaging-delete-sms={{path/to/message_file}}`