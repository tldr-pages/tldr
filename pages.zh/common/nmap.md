# nmap

> 网络探测工具和安全/端口扫描器。
> 某些功能（例如 SYN 扫描）仅在以 root 权限运行 `nmap` 时激活。
> 更多信息：<https://nmap.org/book/man.html>。

- 以不同的 [v]erbosity 级别扫描远程主机的前 1000 个端口：

`nmap -v{{1|2|3}} {{ip_or_hostname}}`

- 对整个子网或单个主机执行非常激进的 ping 扫描：

`nmap -T5 -sn {{192.168.0.0/24|ip_or_hostname1,ip_or_hostname2,...}}`

- 启用操作系统检测、版本检测、脚本扫描和从文件中主机的 traceroute：

`sudo nmap -A -iL {{path/to/file.txt}}`

- 扫描特定的端口列表（使用 `-p-` 来扫描 1 到 65535 的所有端口）：

`nmap -p {{port1,port2,...}} {{ip_or_host1,ip_or_host2,...}}`

- 使用默认的 NSE 脚本对前 1000 个端口进行服务和版本检测，将结果（`-oA`）写入输出文件：

`nmap -sC -sV -oA {{top-1000-ports}} {{ip_or_host1,ip_or_host2,...}}`

- 使用 `default and safe` NSE 脚本仔细扫描目标：

`nmap --script "default and safe" {{ip_or_host1,ip_or_host2,...}}`

- 使用所有可用的 `http-*` NSE 脚本扫描运行在标准端口 80 和 443 上的 Web 服务器：

`nmap --script "http-*" {{ip_or_host1,ip_or_host2,...}} -p 80,443`

- 尝试通过使用极慢的扫描（`-T0`）、诱饵源地址（`-D`）、[f]ragmented 数据包、随机数据和其他方法来规避 IDS/IPS 检测：

`sudo nmap -T0 -D {{decoy_ip1,decoy_ip2,...}} --source-port {{53}} -f --data-length {{16}} -Pn {{ip_or_host}}`