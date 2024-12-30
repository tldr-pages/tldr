# airdecap-ng

> 解密 WEP、WPA 或 WPA2 加密的捕获文件。
> 是 Aircrack-ng 网络软件套件的一部分。
> 更多信息：<https://www.aircrack-ng.org/doku.php?id=airdecap-ng>。

- 从开放网络捕获文件中移除无线报头，并使用接入点的 MAC 地址进行过滤：

`airdecap-ng -b {{ap_mac}} {{path/to/capture.cap}}`

- 使用十六进制格式的密钥解密 [w]EP 加密的捕获文件：

`airdecap-ng -w {{hex_key}} {{path/to/capture.cap}}`

- 使用接入点的 [e]ssid 和 [p]assword 解密 WPA/WPA2 加密的捕获文件：

`airdecap-ng -e {{essid}} -p {{password}} {{path/to/capture.cap}}`

- 使用接入点的 [e]ssid 和 [p]assword 解密 WPA/WPA2 加密的捕获文件，同时保留报头：

`airdecap-ng -l -e {{essid}} -p {{password}} {{path/to/capture.cap}}`

- 使用接入点的 [e]ssid 和 [p]assword 解密 WPA/WPA2 加密的捕获文件，并使用其 MAC 地址进行过滤：

`airdecap-ng -b {{ap_mac}} -e {{essid}} -p {{password}} {{path/to/capture.cap}}`