# ipmitool

> 与智能平台管理接口 (IPMI) 进行交互。
> 更多信息：<https://manned.org/ipmitool>.

- 启动用于本地连接的 IPMI 驱动程序：

`systemctl start ipmidrv`

- 在本地硬件上打开 IPMI shell：

`sudo ipmitool shell`

- 在远程主机上打开 IPMI shell：

`ipmitool -H {{ip_address}} -U {{user_name}} shell`