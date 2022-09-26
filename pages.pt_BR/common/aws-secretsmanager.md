# aws secretsmanager

> Armazena, gerencia, e obtem secrets.
> Mais informações: <https://docs.aws.amazon.com/cli/latest/reference/secretsmanager/>.

- Lista secrets armazenados pelo gerenciador de secretes na conta atual:

`aws secretsmanager list-secrets`

- Cria um secret:

`aws secretsmanager create-secret --name {{nome}} --description "{{descrição_do_secret}}" --secret-string {{secret}}`

- Apaga um secret:

`aws secretsmanager delete-secret --secret-id {{nome_ou_arn}}`

- Visualiza detalhes de um secret menos pelo texto do secret:

`aws secretsmanager describe-secret --secret-id {{nome_ou_arn}}`

- Obtẽm o valor do secret (para pegar a última versão do secret não use `--version-stage`):

`aws secretsmanager get-secret-value --secret-id {{nome_ou_arn}} --version-stage {{versão_do_secret}}`

- Alterna o secret imediatamente usando uma função Lambda:

`aws secretsmanager rotate-secret --secret-id {{nome_ou_arn}} --rotation-lambda-arn {{arn_da_função_lambda}}`

- Alterna o secret automaticamente a cada 30 dias usando uma função Lambda:

`aws secretsmanager rotate-secret --secret-id {{nome_ou_arn}} --rotation-lambda-arn {{arn_da_função_lambda}} --rotation-rules AutomaticallyAfterDays={{30}}`
