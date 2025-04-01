# pyrit

> 使用计算能力破解 WPA/WPA2 的工具。
> 更多信息：<https://manned.org/pyrit>.

- 显示系统破解速度：

`pyrit benchmark`

- 列出可用的核心：

`pyrit list_cores`

- 设置 [e]SSID：

`pyrit -e "{{ESSID}}" create_essid`

- [r]ead 和分析特定的封包捕获文件：

`pyrit -r {{path/to/file.cap|path/to/file.pcap}} analyze`

- 读取并 [i]mport 密码到当前数据库：

`pyrit -i {{path/to/file}} {{import_unique_passwords|unique_passwords|import_passwords}}`

- 将密码 [r]ead 从数据库导出到特定文件：

`pyrit -o {{path/to/file}} export_passwords`

- 使用 Pired Master Keys 转换密码：

`pyrit batch`

- [r]ead 封包文件并破解密码：

`pyrit -r {{path/to/file}} attack_db`
