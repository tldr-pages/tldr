# aws iam

> Interactúa con el Manejo de Identidad y Acceso (o "IAM" en inglés), un servicio web para controlar seguramente el acceso a servicios de AWS.
> Más información: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/index.html>.

- Lista usuarios:

`aws iam list-users`

- Lista políticas:

`aws iam list-policies`

- Lista grupos:

`aws iam list-groups`

- Obtén los usuarios en un grupo:

`aws iam get-group --group-name {{nombre_del_grupo}}`

- Describe una política IAM:

`aws iam get-policy --policy-arn arn:aws:iam::aws:policy/{{nombre_de_política}}`

- Lista claves de acceso:

`aws iam list-access-keys`

- Lista claves de acceso para un usuario específico:

`aws iam list-access-keys --user-name {{usuario}}`

- Muestra ayuda:

`aws iam help`
