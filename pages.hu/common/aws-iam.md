# aws iam

> CLI az AWS IAM-hez. További információ: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/index.html>.

- A `aws iam` súgóoldal megjelenítése (beleértve az összes elérhető iam parancsot):

`aws iam help`

- Felhasználók listázása:

`aws iam list-users`

- List policies:

`aws iam list-policies`

- Csoportok listázása:

`aws iam list-groups`

- Felhasználók lekérdezése egy csoportban:

`aws iam get-group --group-name {{group_name}}`

- IAM házirend leírása:

`aws iam get-policy --policy-arn arn:aws:iam::aws:policy/{{policy_name}}`

- Hozzáférési kulcsok listázása:

`aws iam list-access-keys`

- Hozzáférési kulcsok listázása egy adott felhasználóhoz:

`aws iam list-access-keys --user-name {{user_name}}`
