# masscan

> 用于尽可能快速地进行网络扫描的工具。
> 最好以提升的权限运行。要了解更多 Nmap 兼容性信息，请运行 `masscan --nmap`。
> 更多信息：<https://manned.org/masscan>.

- 扫描指定的 IP 地址或网络子网的 80 端口：

`masscan {{ip_address|network_prefix}} {{[-p|--ports]}} {{80}}`

- 以每秒 100,000 个数据包的速度扫描 B 类子网的前 100 个端口：

`masscan {{10.0.0.0/16}} --top-ports {{100}} --rate {{100000}}`

- 扫描 B 类子网的前 100 个端口，但排除特定排除文件中的范围：

`masscan {{10.0.0.0/16}} --top-ports {{100}} --excludefile {{path/to/file}}`

- 扫描互联网上运行在 80 和 443 端口的 Web 服务器：

`masscan {{0.0.0.0/0}} {{[-p|--ports]}} {{80,443}} --rate {{10000000}}`

- 扫描互联网上运行在 UDP 53 端口的 DNS 服务器：

`masscan {{0.0.0.0/0}} {{[-p|--ports]}} {{U:53}} --rate {{10000000}}`

- 扫描互联网上的特定端口范围，并将结果导出到文件：

`masscan {{0.0.0.0/0}} {{[-p|--ports]}} {{0-65535}} --output-format {{binary|grepable|json|list|xml}} --output-filename {{path/to/file}}`

- 从文件读取二进制扫描结果并输出到 `stdout`：

`masscan --readscan {{path/to/file}}`