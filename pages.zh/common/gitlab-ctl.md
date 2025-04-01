# gitlab-ctl

> 管理 GitLab 全套工具。
> 更多信息：<https://docs.gitlab.com/omnibus/maintenance/>。

- 显示每个服务的状态：

`sudo gitlab-ctl status`

- 显示特定服务的状态：

`sudo gitlab-ctl status {{nginx}}`

- 重启所有服务：

`sudo gitlab-ctl restart`

- 重启特定服务：

`sudo gitlab-ctl restart {{nginx}}`

- 显示所有服务的日志并持续读取直到按 `<Ctrl c>` 键停止：

`sudo gitlab-ctl tail`

- 显示特定服务的日志：

`sudo gitlab-ctl tail {{nginx}}`

- 向特定服务发送 SIGKILL 信号：

`sudo gitlab-ctl kill {{nginx}}`

- 重新配置应用程序：

`sudo gitlab-ctl reconfigure`
