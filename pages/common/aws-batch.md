# aws batch

> Run batch computing workloads through the AWS Batch service.
> More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/index.html>.

- List running batch jobs:

`aws batch list-jobs --job-queue {{queue_name}}`

- Create compute environment:

`aws batch create-compute-environment --compute-environment-name {{compute_environment_name}} --type {{type}}`

- Create batch job queue:

`aws batch create-job-queue --job-queue-name {{queue_name}} --priority {{priority}} --compute-environment-order {{compute_environment}}`

- Submit job:

`aws batch submit-job --job-name {{job_name}} --job-queue {{job_queue}} --job-definition {{job_definition}}`

- Describe the list of batch jobs:

`aws batch describe-jobs --jobs {{jobs}}`

- Cancel job:

`aws batch cancel-job --job-id {{job_id}} --reason {{reason}}`
