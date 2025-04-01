# guacd

> Apache Guacamole 代理守护进程。
> 用于支持客户端插件，实现在 Guacamole 协议和任意远程桌面协议（如 RDP、VNC 等）之间的接口。
> 更多信息：<https://guacamole.apache.org/>。

- 绑定到本地主机的特定端口：

`guacd -b {{127.0.0.1}} -l {{4823}}`

- 以调试模式启动，进程保持在前台：

`guacd -f -L {{debug}}`

- 以 TLS 支持启动：

`guacd -C {{my-cert.crt}} -K {{my-key.pem}}`

- 将 PID 写入文件：

`guacd -p {{path/to/file.pid}}`