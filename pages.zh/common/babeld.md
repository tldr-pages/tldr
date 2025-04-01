# babeld

> 用于 Babel 的路由守护进程，使用防火墙风格的过滤器。
> 更多信息：<https://www.irif.fr/~jch/software/babel/babeld.html>.

- 使用一个或多个 [c]onfiguration 配置文件（按顺序读取）启动守护进程：

`babeld -c {{path/to/ports.conf}} -c {{path/to/filters.conf}} -c {{path/to/interfaces.conf}}`

- 启动后进行 [D]eamonize：

`babeld -D`

- 指定一个 [C]onfiguration 配置命令：

`babeld -C {{'redistribute metric 256'}}`

- 指定要操作的接口：

`babeld {{eth0}} {{eth1}} {{wlan0}}`
