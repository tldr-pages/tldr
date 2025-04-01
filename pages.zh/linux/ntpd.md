# ntpd

> NTP（网络时间协议）守护进程，用于将系统时钟与远程时间服务器或本地参考时钟同步。
> 更多信息：<https://manned.org/ntpd>。

- 启动守护进程：

`sudo ntpd`

- 一次性与远程服务器同步系统时间（同步后退出）：

`sudo ntpd --quit`

- 允许“大”调整的一次性同步：

`sudo ntpd --panicgate --quit`