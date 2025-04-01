# rustscan

> 用 Rust 编写的快速端口扫描器，内置 `nmap`。
> 更多信息：<https://github.com/RustScan/RustScan>.

- 使用默认值扫描一个或多个以逗号分隔的地址的所有端口：

`rustscan {{[-a|--addresses]}} {{ip_or_hostname}}`

- 扫描前 1000 个常见的端口，并检测服务和版本：

`rustscan --top {{[-a|--addresses]}} {{address_or_addresses}}`

- 扫描特定的端口列表：

`rustscan {{[-p|--ports]}} {{port1,port2,...,portN}} {{[-a|--addresses]}} {{address_or_addresses}}`

- 扫描特定范围内的端口：

`rustscan {{[-r|--range]}} {{start-end}} {{[-a|--addresses]}} {{address_or_addresses}}`

- 向 `nmap` 添加脚本参数：

`rustscan {{[-a|--addresses]}} {{address_or_addresses}} -- -A -sC`

- 使用自定义的批次大小（默认：4500）和超时时间（默认：1500ms）进行扫描：

`rustscan {{[-b|--batch-size]}} {{batch_size}} {{[-t|--timeout]}} {{timeout}} {{[-a|--addresses]}} {{address_or_addresses}}`

- 使用特定的端口扫描顺序进行扫描：

`rustscan --scan-order {{serial|random}} {{[-a|--addresses]}} {{address_or_addresses}}`

- 以 grep 格式进行扫描（仅输出端口，不包含 `nmap` 结果）：

`rustscan {{[-g|--greppable]}} {{[-a|--addresses]}} {{address_or_addresses}}`
