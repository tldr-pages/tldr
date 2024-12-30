# Postfix

> Postfix 邮件传输代理 (MTA) 控制程序。
> 另请参见 `dovecot`，一个与 Postfix 集成的邮件投递代理 (MDA)。
> 更多信息：<https://www.postfix.org>。

- 检查配置：

`sudo postfix check`

- 检查 Postfix 守护进程的状态：

`sudo postfix status`

- 启动 Postfix：

`sudo postfix start`

- 优雅地停止 Postfix：

`sudo postfix stop`

- 清空邮件队列：

`sudo postfix flush`

- 重新加载配置文件：

`sudo postfix reload`