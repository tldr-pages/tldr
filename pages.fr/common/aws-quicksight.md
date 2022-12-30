# aws quicksight

> CLI pour AWS QuickSight.
> Accès aux entrées QuickSight.
> Plus d'informations : <https://docs.aws.amazon.com/cli/latest/reference/quicksight/>.

- Liste les datasets:

`aws quicksight list-data-sets --aws-account-id {{id_compte_aws}}`

- Liste les utilisateurs :

`aws quicksight list-users --aws-account-id {{id_compte_aws}} --namespace default`

- Liste les groupes :

`aws quicksight list-groups --aws-account-id {{id_compte_aws}} --namespace default`

- Liste les tableaux de bords :

`aws quicksight list-dashboards --aws-account-id {{id_compte_aws}}`

- Affiche les informations détaillées sur un dataset :

`aws quicksight describe-data-set --aws-account-id {{id_compte_aws}} --data-set-id {{id_data_set}}`

- Affiche les personnes qui peuvent accéder au dataset et quelles actions ils peuvent effectuer sur ce dernier :

`aws quicksight describe-data-set-permissions --aws-account-id {{id_compte_aws}} --data-set-id {{id_data_set}}`
