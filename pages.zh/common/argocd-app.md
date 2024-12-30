# argocd 应用

> 命令行接口用于管理 Argo CD 的应用。
> 更多信息请访问：<https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd_app/>.

- 列出应用：

`argocd app list --output {{json|yaml|wide}}`

- 获取应用详细信息：

`argocd app get {{app_name}} --output {{json|yaml|wide}}`

- 在内部部署应用（到 Argo CD 正在运行的同一集群）：

`argocd app create {{app_name}} --repo {{git_repo_url}} --path {{path/to/repo}} --dest-server https://kubernetes.default.svc --dest-namespace {{ns}}`

- 删除应用：

`argocd app delete {{app_name}}`

- 启用应用自动同步：

`argocd app set {{app_name}} --sync-policy auto --auto-prune --self-heal`

- 预览应用同步而不影响集群：

`argocd app sync {{app_name}} --dry-run --prune`

- 显示应用部署历史：

`argocd app history {{app_name}} --output {{wide|id}}`

- 根据历史 ID 将应用回滚到之前的已部署版本（删除意外资源）：

`argocd app rollback {{app_name}} {{history_id}} --prune`