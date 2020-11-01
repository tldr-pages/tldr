# aws glue

> CLI for AWS Glue.
> Defines the public endpoint for the AWS Glue service.
> More information: <https://docs.aws.amazon.com/cli/latest/reference/glue/index.html>.

- List jobs:

`aws glue list-jobs`

- Start a job:

`aws glue start-job-run --job-name {{job_name}}`

- Start running a workflow:

`aws glue start-workflow-run --name {{workflow_name}}`

- List triggers:

`aws glue list-triggers`

- Start a trigger:

`aws glue start-trigger --name {{trigger_name}}`

- Create a dev endpoint:

`aws glue create-dev-endpoint --endpoint-name {{name}} --role-arn {{role_arn_used_by_endpoint}}`
