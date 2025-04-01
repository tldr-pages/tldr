# gitlab-runner

> 管理 GitLab 跑步机。
> 更多信息：<https://docs.gitlab.com/runner/>。

- 注册一个跑步机：

`sudo gitlab-runner register --url {{https://gitlab.example.com}} --registration-token {{token}} --name {{name}}`

- 使用 Docker 执行器注册一个跑步机：

`sudo gitlab-runner register --url {{https://gitlab.example.com}} --registration-token {{token}} --name {{name}} --executor {{docker}}`

- 注销一个跑步机：

`sudo gitlab-runner unregister --name {{name}}`

- 显示跑步机服务的状态：

`sudo gitlab-runner status`

- 重启跑步机服务：

`sudo gitlab-runner restart`

- 检查已注册的跑步机是否可以连接到 GitLab：

`sudo gitlab-runner verify`