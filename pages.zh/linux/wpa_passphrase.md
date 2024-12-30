# wpa_passphrase

> 从 ASCII 密码短语为 SSID 生成 WPA-PSK 密钥。
> 更多信息：<https://manned.org/wpa_passphrase.1>。

- 从 `stdin` 读取密码短语，计算并显示给定 SSID 的 WPA-PSK 密钥：

`wpa_passphrase {{SSID}}`

- 指定密码短语作为参数，计算并显示给定 SSID 的 WPA-PSK 密钥：

`wpa_passphrase {{SSID}} {{passphrase}}`