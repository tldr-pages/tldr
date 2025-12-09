# airdecap-ng

> 解密 WEP、WPA 或 WPA2 加密的捕获文件。
> 是 Aircrack-ng 网络软件套件的一部分。
> 更多信息：<https://www.aircrack-ng.org/doku.php?id=airdecap-ng>.

- 从开放网络捕获文件中移除无线头，并使用接入点的 MAC 地址进行过滤：

`airdecap-ng -b {{ap_mac}} {{路径/到/捕获文件.cap}}`

- 使用十六进制格式的密钥解密 WEP 加密的捕获文件：

`airdecap-ng -w {{hex_key}} {{路径/到/捕获文件.cap}}`

- 使用接入点的 ESSID 和密码解密 WPA/WPA2 加密的捕获文件：

`airdecap-ng -e {{essid}} -p {{密码}} {{路径/到/捕获文件.cap}}`

- 使用接入点的 ESSID 和密码解密 WPA/WPA2 加密的捕获文件，并保留头部信息：

`airdecap-ng -l -e {{essid}} -p {{密码}} {{路径/到/捕获文件.cap}}`

- 使用接入点的 MAC 地址进行过滤，并使用接入点的 ESSID 和密码解密 WPA/WPA2 加密的捕获文件：

`airdecap-ng -b {{ap_mac}} -e {{essid}} -p {{密码}} {{路径/到/捕获文件.cap}}`
