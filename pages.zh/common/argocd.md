# argocd

> 用于控制 Argo CD 服务器的命令行接口。
> 一些子命令（如 `app`）有各自的使用文档。
> 更多信息：<https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd/>.

- 登录 Argo CD 服务器：

`argocd login --insecure --username {{user}} --password {{password}} {{argocd_server:port}}`

- 列出应用：

`argocd app list`