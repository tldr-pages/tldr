# aws glue

> CLI pentru AWS lipici.
> Definește punctul final public pentru serviciul AWS Lipire.
> Mai multe informaţii: <https://docs.aws.amazon.com/cli/latest/reference/glue/>

- Lista de locuri de muncă:

`aws glue list-jobs`

- Începe un loc de muncă:

`aws glue start-job-run --job-name {{job_name}}`

- Începeți să rulați un flux de lucru:

`aws glue start-workflow-run --name {{workflow_name}}`

- Declanșează lista:

`aws glue list-triggers`

- Porneşte un declanşator:

`aws glue start-trigger --name {{trigger_name}}`

- Creați un punct final dev:

`aws glue create-dev-endpoint --endpoint-name {{name}} --role-arn {{role_arn_used_by_endpoint}}`
