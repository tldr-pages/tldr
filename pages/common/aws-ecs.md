# aws ecs

> Manage Elastic Container Service (ECS) clusters.
> More information: <https://docs.aws.amazon.com/cli/latest/reference/ecs/>.

- List task definitions:

`aws ecs list-task-definitions`

- Describe a task definition:

`aws ecs describe-task-definition --task-definition {{task_definition}}`

- Create a task definition or make a revision:

`aws ecs register-task-definition --cli-input-json file://{{path_to_file.json}}`

- Deregister a task definition marking them INACTIVE:

`aws ecs deregister-task-definition --task-definition {{task_definition}}:{{revision_number}}`

- List services in a specific cluster:

`aws ecs list-services --cluster {{cluster_name}}`

- Describe one or more services in a cluster:

`aws ecs describe-services --services {{service_name}} {{service_name}} --cluster {{cluster_name}}`

- Update a service and force new deployment:

`aws ecs update-service --cluster {{cluster_name}} --service {{service_name}} --task-definition {{task_definition_arn}} --force-new-deployment`

- Wait for service/s to succeed:

`aws ecs wait services-stable --cluster {{cluster_name}} --services {{service_name}} {{service_name}}`
