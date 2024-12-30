# autorecon

> 一款多线程网络侦察工具，能够自动枚举服务。
> 更多信息请访问：<https://github.com/Tib3rius/AutoRecon>。

- 对目标主机进行侦察（详细扫描结果将保存在 `./results` 中）：

`sudo autorecon {{host_or_ip1,host_or_ip2,...}}`

- 从文件中对 [t]arget(s) 进行侦察：

`sudo autorecon --target-file {{path/to/file}}`

- [o]utput 结果到不同的目录：

`sudo autorecon --output {{path/to/results}} {{host_or_ip1,host_or_ip2,...}}`

- 将扫描限制在特定的 [p]orts 和协议（`T` 表示 TCP，`U` 表示 UDP，`B` 表示两者）：

`sudo autorecon --ports {{T:21-25,80,443,U:53,B:123}} {{host_or_ip1,host_or_ip2,...}}`