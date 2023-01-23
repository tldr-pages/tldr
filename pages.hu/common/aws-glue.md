# aws glue

> CLI az AWS Glue-hoz. Meghatározza az AWS Glue szolgáltatás nyilvános végpontját. További információ: <https://docs.aws.amazon.com/cli/latest/reference/glue/>.

- Munkák listázása:

`aws glue list-jobs`

- Egy feladat elindítása:

`aws glue start-job-run --job-name {{job_name}}`

- Egy munkafolyamat futtatásának megkezdése:

`aws glue start-workflow-run --name {{workflow_name}}`

- Triggerek listázása:

`aws glue list-triggers`

- Trigger indítása:

`aws glue start-trigger --name {{trigger_name}}`

- Dev végpont létrehozása:

`aws glue create-dev-endpoint --endpoint-name {{name}} --role-arn {{role_arn_used_by_endpoint}}`
