# aws quicksight

> CLI for AWS QuickSight. Hozzáférés a QuickSight entitásokhoz. További információ: <https://docs.aws.amazon.com/cli/latest/reference/quicksight/>.

- Adatkészletek listázása:

`aws quicksight list-data-sets --aws-account-id {{aws_account_id}}`

- Felhasználók listázása:

`aws quicksight list-users --aws-account-id {{aws_account_id}} --namespace default`

- Csoportok listázása:

`aws quicksight list-groups --aws-account-id {{aws_account_id}} --namespace default`

- Műszerfalak listázása:

`aws quicksight list-dashboards --aws-account-id {{aws_account_id}}`

- Részletes információk megjelenítése egy adatkészletről:

`aws quicksight describe-data-set --aws-account-id {{aws_account_id}} --data-set-id {{data_set_id}}`

- Megjeleníti, hogy ki fér hozzá az adatkészlethez, és milyen műveleteket végezhet az adatkészleten:

`aws quicksight describe-data-set-permissions --aws-account-id {{aws_account_id}} --data-set-id {{data_set_id}}`
