# nmap

> 网络探索工具和安全/端口扫描程序。
> 仅当以特权运行Nmap时，某些功能才激活。
> 更多信息见: <https://nmap.org>.

- 检查IP地址是否可用，并猜测远程主机的操作系统：

`nmap -O {{IP 或者 主机名}}`

- 尝试确定指定的主机是否启动以及它们的名称是什么：

`nmap -sn {{IP 或者 主机名}} {{可选的其它地址}}`

- 像上面一样，如果主机启动了，还可以运行默认的1000端口TCP扫描：:

`nmap {{IP 或者 主机名}} {{可选的其它地址}}`

- 也可以启用脚本，服务检测，操作系统指纹识别和跟踪路由：

`nmap -A {{一个地址 或者 多个地址}}`

- 假设网络连接良好并加快执行速度：

`nmap -T4 {{一个地址 或者 多个地址}}`

- 扫描端口的特定列表（使用-p参数覆盖所有端口, 如 -p 1-65535, 也可以明确指定几个端口，如 -p 3306,3307,3308）：

`nmap -p {{端口1, 端口2, ... , 端口N}} {{一个地址 或者 多个地址}}`

- 执行TCP和UDP扫描（-sU只用UDP扫描，-sZ用SCTP扫描，-sO用于IP扫描）：

`nmap -sSU {{一个地址 或者 多个地址}}`

- Perform full port, service, version detection scan with all default NSE scripts active against a host to determine weaknesses and info:

`nmap -sC -sV {{一个地址 或者 多个地址}}`
