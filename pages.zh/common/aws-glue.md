# aws glue

> AWS Glue 的 CLI。
> 定义 AWS Glue 服务的公共端点。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/glue/>.

- 列出作业：

`aws glue list-jobs`

- 启动作业：

`aws glue start-job-run --job-name {{作业名称}}`

- 启动运行工作流：

`aws glue start-workflow-run --name {{工作流名称}}`

- 列出触发器：

`aws glue list-triggers`

- 启动触发器：

`aws glue start-trigger --name {{触发器名称}}`

- 创建开发端点：

`aws glue create-dev-endpoint --endpoint-name {{名称}} --role-arn {{端点使用的角色_ARN}}`
