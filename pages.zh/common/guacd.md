# guacd

> Apache Guacamole 代理守护进程。
> 客户端插件的支持加载器，用于在 Guacamole 协议与任意远程桌面协议（例如 RDP、VNC、其他）之间进行接口。
> 更多信息：<https://guacamole.apache.org/>.

- 在本地主机的特定端口上绑定：

`guacd -b {{127.0.0.1}} -l {{4823}}`

- 以调试模式启动，保持进程在前台：

`guacd -f -L {{debug}}`

- 启动时支持 TLS：

`guacd -C {{my-cert.crt}} -K {{my-key.pem}}`

- 将 PID 写入文件：

`guacd -p {{path/to/file.pid}}`