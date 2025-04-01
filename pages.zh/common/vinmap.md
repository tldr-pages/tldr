# vinmap

> 一个多线程的 Nmap 扫描器，将 IP 范围分割成块，执行并行扫描，并合并 XML 或 JSON 结果。
> 更多信息：<https://pypi.org/project/vinmap>.

- 扫描子网的基本操作：

`vinmap -ip {{192.168.1.0/24}}`

- 扫描域时启用版本和操作系统检测，并将结果保存到指定文件：

`vinmap -ip {{example.com}} -s "-sV -O" -o {{path/to/scan_results.xml}}`

- 使用 10 个块和 20 个并发线程扫描 IP 范围，不指定时使用系统 CPU 核心的一半：

`vinmap -ip {{10.0.0.1-10.0.0.255}} -n 10 -t 20`

- 以 JSON 格式输出扫描结果：

`vinmap -ip {{192.168.1.1-192.168.1.100}} -f json`

- 使用默认设置扫描多个 IP 并保存合并的 XML 输出：

`vinmap -ip {{192.168.1.1,192.168.1.2,...}}`