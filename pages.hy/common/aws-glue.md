# aws սոսինձ

> CLI AWS սոսինձի համար:.
> Սահմանեք AWS Glue ծառայության հանրային վերջնակետը:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/glue/>:.

- Աշխատանքների ցուցակ.:

`aws glue list-jobs`

- Սկսել աշխատանք.:

`aws glue start-job-run --job-name {{job_name}}`

- Սկսեք գործարկել աշխատանքային հոսքը.:

`aws glue start-workflow-run --name {{workflow_name}}`

- Ցուցակի գործարկիչներ.:

`aws glue list-triggers`

- Սկսեք ձգան.:

`aws glue start-trigger --name {{trigger_name}}`

- Ստեղծեք մշակողի վերջնակետ.:

`aws glue create-dev-endpoint --endpoint-name {{name}} --role-arn {{role_arn_used_by_endpoint}}`
