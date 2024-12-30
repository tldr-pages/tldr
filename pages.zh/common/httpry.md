# httpry

> 一个轻量级的包嗅探器，用于显示和记录HTTP流量。
> 它可以实时运行，显示解析的流量，或作为守护进程运行，将日志记录到输出文件中。
> 更多信息：<https://dumpsterventures.com/jason/httpry/>.

- 将输出保存到文件：

`httpry -o {{path/to/file.log}}`

- 在特定接口上监听并将输出保存为二进制PCAP格式文件：

`httpry {{eth0}} -b {{path/to/file.pcap}}`

- 按逗号分隔的HTTP动词列表过滤输出：

`httpry -m {{get|post|put|head|options|delete|trace|connect|patch}}`

- 从输入捕获文件读取并按IP过滤：

`httpry -r {{path/to/file.log}} '{{host 192.168.5.25}}'`

- 作为守护进程运行：

`httpry -d -o {{path/to/file.log}}`