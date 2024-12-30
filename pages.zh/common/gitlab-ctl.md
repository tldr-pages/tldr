# gitlab-ctl

> 管理 GitLab 包。
> 更多信息：<https://docs.gitlab.com/omnibus/maintenance/>.

- 显示每个服务的状态：

`sudo gitlab-ctl status`

- 显示特定服务的状态：

`sudo gitlab-ctl status {{nginx}}`

- 重启所有服务：

`sudo gitlab-ctl restart`

- 重启特定服务：

`sudo gitlab-ctl restart {{nginx}}`

- 显示所有服务的日志，并持续读取直到按下 `Ctrl + C`：

`sudo gitlab-ctl tail`

- 显示特定服务的日志：

`sudo gitlab-ctl tail {{nginx}}`