# argocd app

> Command-line interface to manage applications by Argo CD.
> More information: <https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd_app/>.

- List applications:

`argocd app list --output {{json|yaml|wide}} `

- Get application details:

`argocd app get {{app_name}} --output {{json|yaml|wide}}`

- Deploy application internally (to the same cluster that Argo CD is running in):

`argocd app create {{app_name}} --repo {{git_repo_url}} --path {{path/to/repo}} --dest-server https://kubernetes.default.svc --dest-namespace {{ns}}`

- Delete an application:

`argocd app delete {{app_name}}`

- Enable application auto-sync:

`argocd app set {{app_name}} --sync-policy auto --auto-prune --self-heal`

- Preview app synchronization without affecting cluster:

`argocd app sync {{app_name}} --dry-run --prune`

- Show application deployment history:

`argocd app history {{app_name}} --output {{wide|id}}`

- Rollback application to a previous deployed version by history ID (deleting unexpected resources):

`argocd app rollback {{app_name}} {{history_id}} --prune`
