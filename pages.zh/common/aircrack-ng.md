# aircrack-ng

> 从捕获的数据包中的握手中破解WEP和WPA/WPA2密钥。
> 是Aircrack-ng网络软件套件的一部分。
> 更多信息：<https://www.aircrack-ng.org/doku.php?id=aircrack-ng>。

- 使用[w]ordlist从捕获文件中破解密钥：

`aircrack-ng -w {{path/to/wordlist.txt}} {{path/to/capture.cap}}`

- 使用[w]ordlist和接入点的[e]ssid从捕获文件中破解密钥：

`aircrack-ng -w {{path/to/wordlist.txt}} -e {{essid}} {{path/to/capture.cap}}`

- 使用[w]ordlist和接入点的MAC地址从捕获文件中破解密钥：

`aircrack-ng -w {{path/to/wordlist.txt}} --bssid {{mac}} {{path/to/capture.cap}}`