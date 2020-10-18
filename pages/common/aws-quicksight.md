# aws quicksight

> CLI for AWS QuickSight - access QuickSight entities.
> More information: <https://docs.aws.amazon.com/cli/latest/reference/quicksight/index.html>.
- Show data-sets:

`aws quicksight list-data-sets --aws-account-id {{aws_account_id}}`

- Show users:

`aws quicksight list-users --aws-account-id {{aws_account_id}} --namespace default`

- Show groups:

`aws quicksight list-groups --aws-account-id {{aws_account_id}} --namespace default`

- Show dashboards:

`aws quicksight list-dashboards --aws-account-id {{aws_account_id}}`

- See details of a dataset such as its input and output columns:

`aws quicksight describe-data-set --aws-account-id {{aws_account_id}} --data-set-id {{data_set_id}}`

- See who has access to the dataset and what kind of actions they can perform on the dataset:

`aws quicksight describe-data-set-permissions --aws-account-id {{aws_account_id}} --data-set-id {{data_set_id}}`
