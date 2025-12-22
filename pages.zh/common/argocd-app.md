# argocd app

> 用于通过 Argo CD 管理应用程序的接口。
> 更多信息：<https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd_app/>.

- 列出应用程序：

`argocd app list --output {{json|yaml|wide}}`

- 获取应用程序详情：

`argocd app get {{app_name}} --output {{json|yaml|wide}}`

- 在内部部署应用程序（部署到 Argo CD 运行所在的同一 Kubernetes 集群中）：

`argocd app create {{app_name}} --repo {{git_repo_url}} --path {{路径/到/仓库}} --dest-server https://kubernetes.default.svc --dest-namespace {{ns}}`

- 删除一个应用程序：

`argocd app delete {{app_name}}`

- 启用应用程序自动同步：

`argocd app set {{app_name}} --sync-policy auto --auto-prune --self-heal`

- 在不影响集群的情况下预览应用程序同步：

`argocd app sync {{app_name}} --dry-run --prune`

- 显示应用程序部署历史记录：

`argocd app history {{app_name}} --output {{wide|id}}`

- 根据历史 ID 回滚应用程序到之前部署的版本（并删除非预期的资源）：

`argocd app rollback {{app_name}} {{history_id}} --prune`
