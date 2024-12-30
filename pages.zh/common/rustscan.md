# rustscan

> 用 Rust 编写的快速端口扫描器，内置 `nmap`。
> 更多信息请访问：<https://github.com/RustScan/RustScan>。

- 使用默认值扫描一个或多个以逗号分隔的 [a]ddresses 的所有端口：

`rustscan --addresses {{ip_or_hostname}}`

- 扫描 [t]op 1000 个端口并进行服务和版本检测：

`rustscan --top --addresses {{address_or_addresses}}`

- 扫描特定的 [p]orts 列表：

`rustscan --ports {{port1,port2,...,portN}} --addresses {{address_or_addresses}}`

- 扫描特定范围的端口：

`rustscan --range {{start-end}} --addresses {{address_or_addresses}}`

- 向 `nmap` 添加脚本参数：

`rustscan --addresses {{address_or_addresses}} -- -A -sC`

- 使用自定义 [b]atch 大小（默认：4500）和 [t]imeout（默认：1500ms）进行扫描：

`rustscan --batch-size {{batch_size}} --timeout {{timeout}} --addresses {{address_or_addresses}}`

- 按特定端口顺序扫描：

`rustscan --scan-order {{serial|random}} --addresses {{address_or_addresses}}`

- 以可 grep 模式扫描（只输出端口，无 `nmap`）：

`rustscan --greppable --addresses {{address_or_addresses}}`