# babeld

> Babel 的路由守护进程，使用防火墙风格的过滤器。
> 更多信息：<https://www.irif.fr/~jch/software/babel/babeld.html>。

- 使用一个或多个 [c]onfiguration 文件启动守护进程（按顺序读取）：

`babeld -c {{path/to/ports.conf}} -c {{path/to/filters.conf}} -c {{path/to/interfaces.conf}}`

- 启动后 [D]eamonize：

`babeld -D`

- 指定一个 [C]onfiguration 命令：

`babeld -C {{'redistribute metric 256'}}`

- 指定在哪些接口上操作：

`babeld {{eth0}} {{eth1}} {{wlan0}}`