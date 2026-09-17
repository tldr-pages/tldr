# aws quicksight

> Crea, elimina, elenca, cerca e aggiorna entità AWS QuickSight.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/quicksight/>.

- Elenca i dataset:

`aws quicksight list-data-sets --aws-account-id {{id_account_aws}}`

- Elenca gli utenti:

`aws quicksight list-users --aws-account-id {{id_account_aws}} --namespace default`

- Elenca i gruppi:

`aws quicksight list-groups --aws-account-id {{id_account_aws}} --namespace default`

- Elenca le dashboard:

`aws quicksight list-dashboards --aws-account-id {{id_account_aws}}`

- Visualizza informazioni dettagliate su un dataset:

`aws quicksight describe-data-set --aws-account-id {{id_account_aws}} --data-set-id {{id_data_set}}`

- Visualizza chi ha accesso al dataset e che tipo di azioni può eseguire sul dataset:

`aws quicksight describe-data-set-permissions --aws-account-id {{id_account_aws}} --data-set-id {{id_data_set}}`
