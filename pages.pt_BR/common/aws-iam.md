# aws iam

> Interage com o Identity and Access Management (IAM), um serviço web para controlar com segurança o acesso aos serviços da AWS.
> Mais informações: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/index.html>.

- Lista os usuários:

`aws iam list-users`

- Lista as políticas:

`aws iam list-policies`

- Lista os grupos:

`aws iam list-groups`

- Obtém os usuários de um grupo:

`aws iam get-group --group-name {{nome_do_grupo}}`

- Descreve uma política do IAM:

`aws iam get-policy --policy-arn arn:aws:iam::aws:policy/{{nome_da_política}}`

- Lista as chaves de acesso:

`aws iam list-access-keys`

- Lista as chaves de acesso para um usuário específico:

`aws iam list-access-keys --user-name {{nome_do_usuário}}`

- Exibe ajuda:

`aws iam help`
