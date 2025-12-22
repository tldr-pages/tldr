# aws sqs

> 为 AWS SQS 服务创建、删除队列并向队列发送消息。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/sqs/>.

- 列出所有可用的队列：

`aws sqs list-queues`

- 显示指定队列的 URL：

`aws sqs get-queue-url --queue-name {{队列名称}}`

- 从 JSON 格式的文件中使用指定属性创建一个队列：

`aws sqs create-queue --queue-name {{队列名称}} --attributes {{file://路径/到/属性文件.json}}`

- 向队列发送一条指定的消息：

`aws sqs send-message --queue-url https://sqs.{{区域}}.amazonaws.com/{{队列名称}} --message-body "{{消息内容}}" --delay-seconds {{延迟时间}} --message-attributes {{file://路径/到/属性文件.json}}`

- 从队列中删除指定的消息：

`aws sqs delete-message --queue-url {{https://队列_URL}} --receipt-handle {{回执句柄}}`

- 删除指定的队列：

`aws sqs delete-queue --queue-url https://sqs.{{区域}}.amazonaws.com/{{队列名称}}`

- 删除指定队列中的所有消息：

`aws sqs purge-queue --queue-url https://sqs.{{区域}}.amazonaws.com/{{队列名称}}`

- 允许指定的 AWS 账户向队列发送消息：

`aws sqs add-permission --queue-url https://sqs.{{区域}}.amazonaws.com/{{队列名称}} --label {{权限名称}} --aws-account-ids {{账户_ID}} --actions SendMessage`
