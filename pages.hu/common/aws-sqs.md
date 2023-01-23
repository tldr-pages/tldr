# aws sqs

> Üzenetek létrehozása, törlése és küldése az AWS SQS szolgáltatás várólistáira. További információk: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/index.html>.

- Az összes rendelkezésre álló várólista listázása:

`aws sqs list-queues`

- Egy adott várólista URL-címének megjelenítése:

`aws sqs get-queue-url --queue-name {{queue_name}}`

- JSON formátumú fájlból meghatározott attribútumokkal rendelkező várólista létrehozása:

`aws sqs create-queue --queue-name {{queue_name}} --attributes {{file://path/to/attributes_file.json}}`

- Egy adott üzenet küldése egy várólistára:

`aws sqs send-message --queue-url https://sqs.{{region}}.amazonaws.com/{{queue_name}} --message-body "{{message_body}}" --delay-seconds {{delay}} --message-attributes {{file://path/to/attributes_file.json}}`

- Megadott üzenet törlése egy várólistából:

`aws sqs delete-message --queue-url {{https://queue_url}} --receipt-handle {{receipt_handle}}`

- Egy adott várólista törlése:

`aws sqs delete-queue --queue-url https://sqs.{{region}}.amazonaws.com/{{queue_name}}`

- Az összes üzenet törlése a megadott várólistából:

`aws sqs purge-queue --queue-url https://sqs.{{region}}.amazonaws.com/{{queue_name}}`

- Egy adott AWS-fiók engedélyezése üzenetek küldésére a várólistába:

`aws sqs add-permission --queue-url https://sqs.{{region}}.amazonaws.com/{{queue_name}} --label {{permission_name}} --aws-account-ids {{account_id}} --actions SendMessage`
