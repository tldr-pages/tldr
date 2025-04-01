# nbtscan

> 扫描网络以获取 NetBIOS 名称信息。
> 更多信息：<https://github.com/resurrecting-open-source-projects/nbtscan>.

- 扫描网络以获取 NetBIOS 名称：

`nbtscan {{192.168.0.1/24}}`

- 扫描单个 IP 地址：

`nbtscan {{192.168.0.1}}`

- 显示详细输出：

`nbtscan -v {{192.168.0.1/24}}`

- 以 `/etc/hosts` 格式显示输出：

`nbtscan -e {{192.168.0.1/24}}`

- 从文件中读取要扫描的 IP 地址/网络：

`nbtscan -f {{path/to/file.txt}}`