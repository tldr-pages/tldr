# gitlab-runner

> 管理 GitLab 运行器。
> 更多信息：<https://docs.gitlab.com/runner/>.

- 注册一个运行器：

`sudo gitlab-runner register --url {{https://gitlab.example.com}} --registration-token {{token}} --name {{name}}`

- 使用 Docker 执行器注册一个运行器：

`sudo gitlab-runner register --url {{https://gitlab.example.com}} --registration-token {{token}} --name {{name}} --executor {{docker}}`

- 注销一个运行器：

`sudo gitlab-runner unregister --name {{name}}`

- 显示运行器服务的状态：

`sudo gitlab-runner status`

- 重启运行器服务：

`sudo gitlab-runner restart`

- 检查已注册的运行器是否能够连接到 GitLab：

`sudo gitlab-runner verify`