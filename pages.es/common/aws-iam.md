# aws iam

> CLI para AWS IAM.
> Más información: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/index.html>.

- Muestra la página de ayuda de `aws iam` (incluyendo todos los comandos iam disponibles):

`aws iam help`

- Lista usuarios:

`aws iam list-users`

- Lista políticas:

`aws iam list-policies`

- Lista grupos:

`aws iam list-groups`

- Obtiene los usuarios de un grupo:

`aws iam get-group --group-name {{nombre_grupo}}`

- Describe una política IAM:

`aws iam get-policy --policy-arn arn:aws:iam::aws:policy/{{nombre_de_politica}}`

- Lista claves de acceso:

`aws iam list-access-keys`

- Lista claves de acceso para un usuario específico:

`aws iam list-access-keys --user-name {{nombre_usuario}}`
