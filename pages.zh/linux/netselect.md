# netselect

> 用于选择快速网络服务器的速度测试。
> 更多信息：<https://github.com/apenwarr/netselect>。

- 选择具有最低延迟的服务器：

`sudo netselect {{host_1}} {{host_2}}`

- 显示名称服务器解析和统计信息：

`sudo netselect -vv {{host_1}} {{host_2}}`

- 定义最大 TTL（生存时间）：

`sudo netselect -m {{10}} {{host_1}} {{host_2}}`

- 打印主机中最快的 `n` 个服务器：

`sudo netselect -s {{n}} {{host_1}} {{host_2}} {{host_3}}`

- 显示帮助：

`netselect`