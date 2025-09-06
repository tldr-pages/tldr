# aircrack-ng

> 破解捕获数据包中握手阶段的 WEP 和 WPA/WPA2 密钥。
> Aircrack-ng 网络软件套件的一部分。
> 更多信息：<https://www.aircrack-ng.org/doku.php?id=aircrack-ng>.

- 使用字典文件破解捕获文件中的密钥：

`aircrack-ng -w {{路径/到/字典文件.txt}} {{路径/到/捕获文件.cap}}`

- 使用多线程和字典文件破解捕获文件中的密钥：

`aircrack-ng -p {{线程数}} -w {{路径/到/字典文件.txt}} {{路径/到/捕获文件.cap}}`

- 使用字典文件和接入点的 ESSID 破解捕获文件中的密钥：

`aircrack-ng -w {{路径/到/字典文件.txt}} -e {{essid}} {{路径/到/捕获文件.cap}}`

- 使用字典文件和接入点的 MAC 地址破解捕获文件中的密钥：

`aircrack-ng -w {{路径/到/字典文件.txt}} --bssid {{mac}} {{路径/到/捕获文件.cap}}`
