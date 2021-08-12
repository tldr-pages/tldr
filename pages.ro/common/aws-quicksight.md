# aws quicksight

> CLI pentru AWS QuickSight.
> Accesați entități QuickSight.
> Mai multe informaţii: <https://docs.aws.amazon.com/cli/latest/reference/quicksight/>

- Lista seturilor de date:

`aws quicksight list-data-sets --aws-account-id {{aws_account_id}}`

- Lista utilizatorilor:

`aws quicksight list-users --aws-account-id {{aws_account_id}} --namespace default`

- Lista grupurilor:

`aws quicksight list-groups --aws-account-id {{aws_account_id}} --namespace default`

- Lista tablourilor de bord:

`aws quicksight list-dashboards --aws-account-id {{aws_account_id}}`

- Afișează informații detaliate despre un set de date:

`aws quicksight describe-data-set --aws-account-id {{aws_account_id}} --data-set-id {{data_set_id}}`

- Afișați cine are acces la setul de date și ce fel de acțiuni pot efectua pe setul de date:

`aws quicksight describe-data-set-permissions --aws-account-id {{aws_account_id}} --data-set-id {{data_set_id}}`
