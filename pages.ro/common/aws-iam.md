# aws iam

> CLI pentru AWS IAM.
> Mai multe informaţii: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/index.html>

- Arată pagina de ajutor `aws iam` (inclusiv toate comenzile iam disponibile):

`aws iam help`

- Lista utilizatorilor:

`aws iam list-users`

- Lista de politici:

`aws iam list-policies`

- Lista grupurilor:

`aws iam list-groups`

- Obțineți utilizatori într-un grup:

`aws iam get-group --group-name {{group_name}}`

- Descrieți o politică IAM:

`aws iam get-policy --policy-arn arn:aws:iam::aws:policy/{{policy_name}}`

- Cheile de acces la listă:

`aws iam list-access-keys`

- Lista cheilor de acces pentru un anumit utilizator:

`aws iam list-access-keys --user-name {{user_name}}`
