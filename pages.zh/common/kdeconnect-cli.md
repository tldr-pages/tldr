# kdeconnect-cli

> 使用 KDE Connect 在设备之间共享文件或文本，响铃，解锁等。
> 更多信息：<https://kdeconnect.kde.org>.

- 列出所有设备：

`kdeconnect-cli --list-devices`

- 列出可用（已配对且可访问）的设备：

`kdeconnect-cli --list-available`

- 请求与特定设备配对，指定其 ID：

`kdeconnect-cli --pair --device {{device_id}}`

- 使特定设备发出铃声，指定其名称：

`kdeconnect-cli --ring --name "{{device_name}}"`

- 与已配对的设备共享 URL 或文件，指定其 ID：

`kdeconnect-cli --share {{url|path/to/file}} --device {{device_id}}`

- 向特定号码发送带有可选附件的 SMS：

`kdeconnect-cli --name "{{device_name}}" --send-sms "{{message}}" --destination {{phone_number}} --attachment {{path/to/file}}`

- 解锁特定设备：

`kdeconnect-cli --name "{{device_name}}" --unlock`

- 在特定设备上模拟按键：

`kdeconnect-cli --name "{{device_name}}" --send-keys {{key}}`
