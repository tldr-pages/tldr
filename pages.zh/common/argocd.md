# argocd

> 控制 Argo CD 服务器的接口。
> 某些子命令（如 `app`）有自己的使用文档。
> 更多信息：<https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd/>。

- 登录 Argo CD 服务器：

`argocd login --insecure --username {{用户}} --password {{密码}} {{argocd_server:port}}`

- 列出应用程序：

`argocd app list`
