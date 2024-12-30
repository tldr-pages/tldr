# pyrit

> 使用计算能力的WPA/WPA2破解工具。
> 更多信息请访问：<https://github.com/JPaulMora/Pyrit>。

- 显示系统破解速度：

`pyrit benchmark`

- 列出可用核心：

`pyrit list_cores`

- 设置[e]SSID：

`pyrit -e "{{ESSID}}" create_essid`

- [r]ead和分析特定的抓包文件：

`pyrit -r {{path/to/file.cap|path/to/file.pcap}} analyze`

- 阅读并[i]mport密码到当前数据库：

`pyrit -i {{path/to/file}} {{import_unique_passwords|unique_passwords|import_passwords}}`

- Exp[o]rt数据库中的密码到特定文件：

`pyrit -o {{path/to/file}} export_passwords`

- 使用Pired Master Keys翻译密码：

`pyrit batch`

- [r]ead抓包文件并破解密码：

`pyrit -r {{path/to/file}} attack_db`