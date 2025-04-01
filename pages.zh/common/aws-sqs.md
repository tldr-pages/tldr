# aws sqs

> 创建、删除和发送消息到 AWS SQS 服务中的队列。
> 更多信息：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/index.html>.

- 列出所有可用的队列：

`aws sqs list-queues`

- 显示特定队列的 URL：

`aws sqs get-queue-url --queue-name {{queue_name}}`

- 从 JSON 格式的文件中创建具有特定属性的队列：

`aws sqs create-queue --queue-name {{queue_name}} --attributes {{file://path/to/attributes_file.json}}`

- 向队列发送特定的消息：

`aws sqs send-message --queue-url https://sqs.{{region}}.amazonaws.com/{{queue_name}} --message-body "{{message_body}}" --delay-seconds {{delay}} --message-attributes {{file://path/to/attributes_file.json}}`

- 从队列中删除指定的消息：

`aws sqs delete-message --queue-url {{https://queue_url}} --receipt-handle {{receipt_handle}}`

- 删除特定的队列：

`aws sqs delete-queue --queue-url https://sqs.{{region}}.amazonaws.com/{{queue_name}}`

- 删除指定队列中的所有消息：

`aws sqs purge-queue --queue-url https://sqs.{{region}}.amazonaws.com/{{queue_name}}`

- 允许特定的 AWS 账户向队列发送消息：

`aws sqs add-permission --queue-url https://sqs.{{region}}.amazonaws.com/{{queue_name}} --label {{permission_name}} --aws-account-ids {{account_id}} --actions SendMessage`
