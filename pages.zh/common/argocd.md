# argocd

> 控制 Argo CD 服务器的命令行界面。
> 一些子命令如 `app` 有自己的使用文档。
> 更多信息：<https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd/>。

- 登录到 Argo CD 服务器：

`argocd login --insecure --username {{user}} --password {{password}} {{argocd_server:port}}`

- 列出应用程序：

`argocd app list`