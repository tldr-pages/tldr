# aws քառ

> Ստեղծեք, ջնջեք և ուղարկեք հաղորդագրություններ AWS SQS ծառայության հերթերին:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/sqs/>:.

- Նշեք բոլոր հասանելի հերթերը.:

`aws sqs list-queues`

- Ցուցադրել կոնկրետ հերթի URL-ը.:

`aws sqs get-queue-url --queue-name {{queue_name}}`

- JSON ձևաչափով ֆայլից ստեղծեք որոշակի ատրիբուտներով հերթ.:

`aws sqs create-queue --queue-name {{queue_name}} --attributes {{file://path/to/attributes_file.json}}`

- Ուղարկեք կոնկրետ հաղորդագրություն հերթին.:

`aws sqs send-message --queue-url https://sqs.{{region}}.amazonaws.com/{{queue_name}} --message-body "{{message_body}}" --delay-seconds {{delay}} --message-attributes {{file://path/to/attributes_file.json}}`

- Ջնջել նշված հաղորդագրությունը հերթից.:

`aws sqs delete-message --queue-url {{https://queue_url}} --receipt-handle {{receipt_handle}}`

- Ջնջել որոշակի հերթ.:

`aws sqs delete-queue --queue-url https://sqs.{{region}}.amazonaws.com/{{queue_name}}`

- Ջնջել բոլոր հաղորդագրությունները նշված հերթից.:

`aws sqs purge-queue --queue-url https://sqs.{{region}}.amazonaws.com/{{queue_name}}`

- Միացրեք որոշակի AWS հաշիվ՝ հաղորդագրություններ հերթագրելու համար.:

`aws sqs add-permission --queue-url https://sqs.{{region}}.amazonaws.com/{{queue_name}} --label {{permission_name}} --aws-account-ids {{account_id}} --actions SendMessage`
