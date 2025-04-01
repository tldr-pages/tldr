# ipmitool

> 与智能平台管理接口 (IPMI) 交互。
> 更多信息：<https://man.freebsd.org/cgi/man.cgi?query=ipmitool>.

- 加载 IPMI 内核模块以进行本地连接：

`kldload ipmi.ko`

- 在本地硬件上打开 IPMI shell：

`ipmitool shell`

- 在远程主机上打开 IPMI shell：

`ipmitool -H {{ip_address}} -U {{user_name}} shell`