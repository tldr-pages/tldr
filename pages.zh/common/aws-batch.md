# aws batch

> 通过 AWS Batch 服务运行批量计算工作负载。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/batch/>.

- 列出正在运行的批处理作业：

`aws batch list-jobs --job-queue {{队列名称}}`

- 创建计算环境：

`aws batch create-compute-environment --compute-environment-name {{计算环境名称}} --type {{类型}}`

- 创建批处理作业队列：

`aws batch create-job-queue --job-queue-name {{队列名称}} --priority {{优先级}} --compute-environment-order {{计算环境}}`

- 提交作业：

`aws batch submit-job --job-name {{作业名称}} --job-queue {{作业队列}} --job-definition {{作业定义}}`

- 描述批处理作业列表：

`aws batch describe-jobs --jobs {{作业}}`

- 取消作业：

`aws batch cancel-job --job-id {{作业 ID}} --reason {{原因}}`
