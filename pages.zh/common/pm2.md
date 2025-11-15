# pm2

> Node.js 的进程管理工具。
> 用于日志管理、监控和配置进程。
> 更多信息：<https://pm2.keymetrics.io>.

- 启动一个进程并指定名称，以便后续操作使用：

`pm2 start {{app.js}} --name {{应用名称}}`

- 列出所有进程：

`pm2 list`

- 监控所有进程：

`pm2 monit`

- 停止一个进程：

`pm2 stop {{应用名称}}`

- 重启一个进程：

`pm2 restart {{应用名称}}`

- 保存当前所有进程，便于稍后恢复：

`pm2 save`

- 恢复之前保存的进程：

`pm2 resurrect`
