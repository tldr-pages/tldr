# AWS Glue

> AWS Glue 的命令行界面。
> 定义 AWS Glue 服务的公共端点。
> 更多信息请访问：<https://docs.aws.amazon.com/cli/latest/reference/glue/>。

- 列出作业：

`aws glue list-jobs`

- 启动作业：

`aws glue start-job-run --job-name {{job_name}}`

- 启动工作流：

`aws glue start-workflow-run --name {{workflow_name}}`

- 列出触发器：

`aws glue list-triggers`

- 启动触发器：

`aws glue start-trigger --name {{trigger_name}}`

- 创建开发端点：

`aws glue create-dev-endpoint --endpoint-name {{name}} --role-arn {{role_arn_used_by_endpoint}}`