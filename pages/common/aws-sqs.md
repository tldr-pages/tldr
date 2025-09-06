# aws sqs

> Create, delete, and send messages to queues for the AWS SQS service.
> More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/index.html>.

- List all availables queues:

`aws sqs list-queues`

- Display the URL of a specific queue:

`aws sqs get-queue-url --queue-name {{queue_name}}`

- Create a queue with specific attributes from a file in JSON format:

`aws sqs create-queue --queue-name {{queue_name}} --attributes {{file://path/to/attributes_file.json}}`

- Send a specific message to a queue:

`aws sqs send-message --queue-url https://sqs.{{region}}.amazonaws.com/{{queue_name}} --message-body "{{message_body}}" --delay-seconds {{delay}} --message-attributes {{file://path/to/attributes_file.json}}`

- Delete the specified message from a queue:

`aws sqs delete-message --queue-url {{https://queue_url}} --receipt-handle {{receipt_handle}}`

- Delete a specific queue:

`aws sqs delete-queue --queue-url https://sqs.{{region}}.amazonaws.com/{{queue_name}}`

- Delete all messages from the specified queue:

`aws sqs purge-queue --queue-url https://sqs.{{region}}.amazonaws.com/{{queue_name}}`

- Enable a specific AWS account to send messages to queue:

`aws sqs add-permission --queue-url https://sqs.{{region}}.amazonaws.com/{{queue_name}} --label {{permission_name}} --aws-account-ids {{account_id}} --actions SendMessage`
