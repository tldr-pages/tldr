# masscan

> 用于尽可能快速扫描的网络扫描仪。
> 最好以提升的权限运行。与Nmap兼容，运行 `masscan --nmap` 以了解更多信息。
> 更多信息请访问: <https://github.com/robertdavidgraham/masscan>。

- 扫描某个IP或网络子网的 [p]ort 80：

`masscan {{ip_address|network_prefix}} --ports {{80}}`

- 以每秒100,000个数据包的速度扫描一个B类子网的前100个端口：

`masscan {{10.0.0.0/16}} --top-ports {{100}} --rate {{100000}}`

- 扫描一个B类子网，避免来自特定排除文件的范围：

`masscan {{10.0.0.0/16}} --top-ports {{100}} --excludefile {{path/to/file}}`

- 在互联网上扫描运行在80和443端口的Web服务器：

`masscan {{0.0.0.0/0}} --ports {{80,443}} --rate {{10000000}}`

- 在互联网上扫描运行在UDP 53端口的DNS服务器：

`masscan {{0.0.0.0/0}} --ports {{U:53}} --rate {{10000000}}`

- 在互联网上扫描特定端口范围并导出到文件：

`masscan {{0.0.0.0/0}} --ports {{0-65535}} --output-format {{binary|grepable|json|list|xml}} --output-filename {{path/to/file}}`

- 从文件读取二进制扫描结果并输出到 `stdout`：

`masscan --readscan {{path/to/file}}`