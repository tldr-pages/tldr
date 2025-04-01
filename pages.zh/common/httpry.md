# httpry

> 一个轻量级的包嗅探器，用于显示和记录 HTTP 流量。
> 它可以实时运行，边解析边显示流量，也可以作为守护进程运行并将日志记录到输出文件。
> 更多信息：<https://dumpsterventures.com/jason/httpry/>.

- 将输出保存到文件：

`httpry -o {{path/to/file.log}}`

- 在特定接口上监听并将输出保存为二进制 PCAP 格式文件：

`httpry {{eth0}} -b {{path/to/file.pcap}}`

- 通过逗号分隔的 HTTP 方法列表过滤输出：

`httpry -m {{get|post|put|head|options|delete|trace|connect|patch}}`

- 从输入捕获文件中读取并按 IP 过滤：

`httpry -r {{path/to/file.log}} '{{host 192.168.5.25}}'`

- 作为守护进程运行：

`httpry -d -o {{path/to/file.log}}`
