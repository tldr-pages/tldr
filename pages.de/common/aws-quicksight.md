# aws quicksight

> Kommandozeilen Werkzeug für AWS QuickSight.
> Mehr Informationen: <https://docs.aws.amazon.com/cli/latest/reference/quicksight/index.html>.

- Auflistung aller Datensätze:

`aws quicksight list-data-sets --aws-account-id {{aws_account_id}}`

- Auflistung aller Benutzer:

`aws quicksight list-users --aws-account-id {{aws_account_id}} --namespace default`

- Auflistung aller Gruppen:

`aws quicksight list-groups --aws-account-id {{aws_account_id}} --namespace default`

- Auflistung aller Dashboards:

`aws quicksight list-dashboards --aws-account-id {{aws_account_id}}`

- Detail-Auflistung eines Datensatzes:

`aws quicksight describe-data-set --aws-account-id {{aws_account_id}} --data-set-id {{data_set_id}}`

- Auflistung der Zugängsberechtungen zu einem Datensatz:

`aws quicksight describe-data-set-permissions --aws-account-id {{aws_account_id}} --data-set-id {{data_set_id}}`
