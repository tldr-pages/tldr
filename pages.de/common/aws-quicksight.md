# aws quicksight

> CLI für AWS QuickSight.
> Weitere Informationen: <https://docs.aws.amazon.com/cli/latest/reference/quicksight/>.

- Liste alle Datensätze auf:

`aws quicksight list-data-sets --aws-account-id {{aws_account_id}}`

- Liste alle Benutzer auf:

`aws quicksight list-users --aws-account-id {{aws_account_id}} --namespace default`

- Liste alle Gruppen auf:

`aws quicksight list-groups --aws-account-id {{aws_account_id}} --namespace default`

- Liste alle Dashboards auf:

`aws quicksight list-dashboards --aws-account-id {{aws_account_id}}`

- Liste einen Datensatz detailliert aus:

`aws quicksight describe-data-set --aws-account-id {{aws_account_id}} --data-set-id {{datensatz_id}}`

- Liste Zugangsberechtigungen zu einem Datensatz auf:

`aws quicksight describe-data-set-permissions --aws-account-id {{aws_account_id}} --data-set-id {{datensatz_id}}`
