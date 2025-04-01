# vela

> 用于 Vela 管道的命令行工具。
> 更多信息：<https://go-vela.github.io/docs/reference/cli/>.

- 从 Git 分支、提交或标签触发管道运行：

`vela add deployment --org {{organization}} --repo {{repository_name}} --target {{environment}} --ref {{branch|commit|refs/tags/git_tag}} --description "{{deploy_description}}"`

- 列出仓库的部署：

`vela get deployment --org {{organization}} --repo {{repository_name}}`

- 查看特定部署的详细信息：

`vela view deployment --org {{organization}} --repo {{repository_name}} --deployment {{deployment_number}}`