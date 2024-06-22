# aircrack-ng

> 破解捕获数据包中的握手时段的 WEP 和 WPA/WPA2 密钥。
> 是 Aircrack-ng 网络软件套件的一部分。
> 更多信息： <https://www.aircrack-ng.org/doku.php?id=aircrack-ng>。

- 使用字典文件破解捕获文件中的密钥：

`aircrack-ng -w {{path/to/wordlist.txt}} {{path/to/capture.cap}}`

- 使用字典文件和接入点的 ESSID 破解捕获文件中的密钥：

`aircrack-ng -w {{path/to/wordlist.txt}} -e {{essid}} {{path/to/capture.cap}}`

- 使用字典文件和接入点的 MAC 地址破解捕获文件中的密钥：

`aircrack-ng -w {{path/to/wordlist.txt}} --bssid {{mac}} {{path/to/capture.cap}}`
