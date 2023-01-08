# aws iam

> CLI for AWS IAM.
> Mais informações: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/index.html>.

- Exibe a página de ajuda do `aws iam` (incluindo todos os comandos iam disponíveis):

`aws iam help`

- Lista os usuários:

`aws iam list-users`

- Lista as políticas:

`aws iam list-policies`

- Lista os grupos:

`aws iam list-groups`

- Obtém os usuários de um grupo:

`aws iam get-group --group-name {{nome_do_grupo}}`

- Descreve uma política IAM:

`aws iam get-policy --policy-arn arn:aws:iam::aws:policy/{{nome_da_política}}`

- Lista as chaves de acesso:

`aws iam list-access-keys`

- Lista as chaves de acesso para um usuário específico:

`aws iam list-access-keys --user-name {{nome_do_usuário}}`
