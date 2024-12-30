# pm2

> Node.js 的进程管理器。
> 用于日志管理、监控和配置进程。
> 更多信息：<https://pm2.keymetrics.io>。

- 使用可用于后续操作的名称启动进程：

`pm2 start {{app.js}} --name {{application_name}}`

- 列出进程：

`pm2 list`

- 监控所有进程：

`pm2 monit`

- 停止一个进程：

`pm2 stop {{application_name}}`

- 重启一个进程：

`pm2 restart {{application_name}}`

- 保存所有进程以便以后恢复：

`pm2 save`

- 恢复之前保存的进程：

`pm2 resurrect`