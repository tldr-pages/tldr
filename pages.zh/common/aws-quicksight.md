# aws quicksight

> 创建、删除、列出、搜索和更新 AWS QuickSight 实体。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/quicksight/>.

- 列出数据集：

`aws quicksight list-data-sets --aws-account-id {{AWS 账户 ID}}`

- 列出用户：

`aws quicksight list-users --aws-account-id {{AWS 账户 ID}} --namespace default`

- 列出组：

`aws quicksight list-groups --aws-account-id {{AWS 账户 ID}} --namespace default`

- 列出仪表板：

`aws quicksight list-dashboards --aws-account-id {{AWS 账户 ID}}`

- 显示数据集的详细信息：

`aws quicksight describe-data-set --aws-account-id {{AWS 账户 ID}} --data-set-id {{数据集 ID}}`

- 显示谁可以访问该数据集，以及他们可以对该数据集执行哪些操作：

`aws quicksight describe-data-set-permissions --aws-account-id {{AWS 账户 ID}} --data-set-id {{数据集 ID}}`
