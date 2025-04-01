# aws quicksight

> 创建、删除、列出、搜索和更新 AWS QuickSight 实体。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/quicksight/>.

- 列出数据集：

`aws quicksight list-data-sets --aws-account-id {{aws_account_id}}`

- 列出用户：

`aws quicksight list-users --aws-account-id {{aws_account_id}} --namespace default`

- 列出组：

`aws quicksight list-groups --aws-account-id {{aws_account_id}} --namespace default`

- 列出仪表板：

`aws quicksight list-dashboards --aws-account-id {{aws_account_id}}`

- 显示数据集的详细信息：

`aws quicksight describe-data-set --aws-account-id {{aws_account_id}} --data-set-id {{data_set_id}}`

- 显示对数据集具有访问权限的用户及其可执行的操作：

`aws quicksight describe-data-set-permissions --aws-account-id {{aws_account_id}} --data-set-id {{data_set_id}}`