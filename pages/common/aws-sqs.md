# aws sqs

> CLI for AWS SQS -  provides simple queue for storing messages to share it between applications.
> More information: <https://docs.aws.amazon.com/cli/latest/reference/sqs/>.

- List all availables queues:

`aws sqs list-queues`

- Get a queue url:

`aws sqs get-queue-url --queue-name {{queue_name}}`

- Create queue with specified name:

`aws sqs create-queue --queue-name {{queue_name}} --attributes file://{{queue_atributes_file.json}}`

- Send message to queue:

`aws sqs send-message --queue-url {{https://sqs.us-east-1.amazonaws.com/my_queue}} --message-body "{{My message body}}" --delay-seconds {{##}} --message-attributes file://{{my-message.json}}`

- Delete specified message from queue:

`aws sqs delete-message --queue-url {{https://queue_url}} --receipt-handle {{message_receipt-handle}}`

- Delete specific queue:

`aws sqs delete-queue --queue-url {{https://sqs.us-east-1.amazonaws.com/my_queue}}`

- Delete All messages in specified queue:

`aws sqs purge-queue --queue-url {{https://sqs.us-east-1.amazonaws.com/my_queue}}`

- Enable AWS account to send messages to queue:

`aws sqs add-permission --queue-url {{https://sqs.us-east-1.amazonaws.com/my_queue}} --label {{sendMessagesPermission}} --aws-account-ids {{AWS-ACCOUNT-ID}} --actions SendMessage`
