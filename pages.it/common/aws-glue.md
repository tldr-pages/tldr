# aws glue

> CLI per AWS Glue.
> Definisce l'endpoint pubblico per il servizio AWS Glue.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/glue/>.

- Elenca i job:

`aws glue list-jobs`

- Avvia un job:

`aws glue start-job-run --job-name {{nome_job}}`

- Avvia l'esecuzione di un workflow:

`aws glue start-workflow-run --name {{nome_workflow}}`

- Elenca i trigger:

`aws glue list-triggers`

- Avvia un trigger:

`aws glue start-trigger --name {{nome_trigger}}`

- Crea un endpoint di sviluppo:

`aws glue create-dev-endpoint --endpoint-name {{nome}} --role-arn {{role_arn_used_by_endpoint}}`
