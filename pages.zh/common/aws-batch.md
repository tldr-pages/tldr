# aws batch

> 通过 AWS Batch 服务运行批处理计算工作负载。
> 更多信息：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/index.html>.

- 列出正在运行的批处理作业：

`aws batch list-jobs --job-queue {{queue_name}}`

- 创建计算环境：

`aws batch create-compute-environment --compute-environment-name {{compute_environment_name}} --type {{type}}`

- 创建批处理作业队列：

`aws batch create-job-queue --job-queue-name {{queue_name}} --priority {{priority}} --compute-environment-order {{compute_environment}}`

- 提交作业：

`aws batch submit-job --job-name {{job_name}} --job-queue {{job_queue}} --job-definition {{job_definition}}`

- 描述批处理作业列表：

`aws batch describe-jobs --jobs {{jobs}}`

- 取消作业：

`aws batch cancel-job --job-id {{job_id}} --reason {{reason}}`