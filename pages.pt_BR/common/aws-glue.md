# aws glue

> Linha de comando CLI para o AWS Glue.
> Define o endpoint público para o servico AWS Glue.
> Mais informações: <https://docs.aws.amazon.com/cli/latest/reference/glue/>.

- Lista trabalhos:

`aws glue list-jobs`

- Inicia um trabalho:

`aws glue start-job-run --job-name {{nome_do_trabalho}}`

- Inicia um fluxo de trabalho:

`aws glue start-workflow-run --name {{nome_do_fluxo_de_trabalho}}`

- Lista os gatilhos:

`aws glue list-triggers`

- Iniciar um gatilho:

`aws glue start-trigger --name {{nome_do_gatilho}}`

- Cria um endpoint de desenvolvimento:

`aws glue create-dev-endpoint --endpoint-name {{nome}} --role-arn {{papel_arn_usado_pelo_endpoint}}`
