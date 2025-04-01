# autorecon

> 一个多线程网络侦察工具，可自动枚举服务。
> 更多信息：<https://github.com/Tib3rius/AutoRecon>.

- 对目标主机（或多个主机）进行侦察（详细的扫描结果将保存在 `./results` 目录中）：

`sudo autorecon {{host_or_ip1,host_or_ip2,...}}`

- 从文件中读取目标进行侦察：

`sudo autorecon {{[-t|--target-file]}} {{path/to/file}}`

- 将结果输出到不同的目录：

`sudo autorecon {{[-o|--output]}} {{path/to/results}} {{host_or_ip1,host_or_ip2,...}}`

- 限制扫描特定端口和协议（`T` 表示 TCP，`U` 表示 UDP，`B` 表示两者都包括）：

`sudo autorecon {{[-p|--ports]}} {{T:21-25,80,443,U:53,B:123}} {{host_or_ip1,host_or_ip2,...}}`
