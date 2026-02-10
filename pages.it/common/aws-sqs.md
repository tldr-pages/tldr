# aws sqs

> Crea, elimina e invia messaggi alle code per il servizio AWS SQS.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/sqs/>.

- Elenca tutte le code disponibili:

`aws sqs list-queues`

- Visualizza l'URL di una coda specifica:

`aws sqs get-queue-url --queue-name {{nome_coda}}`

- Crea una coda con attributi specifici da un file in formato JSON:

`aws sqs create-queue --queue-name {{nome_coda}} --attributes {{file://percorso/del/attributes_file.json}}`

- Invia un messaggio specifico a una coda:

`aws sqs send-message --queue-url https://sqs.{{regione}}.amazonaws.com/{{nome_coda}} --message-body "{{body_messaggio}}" --delay-seconds {{ritardo}} --message-attributes {{file://percorso/del/attributes_file.json}}`

- Elimina il messaggio specificato da una coda:

`aws sqs delete-message --queue-url {{https://url_coda}} --receipt-handle {{receipt_handle}}`

- Elimina una coda specifica:

`aws sqs delete-queue --queue-url https://sqs.{{regione}}.amazonaws.com/{{nome_coda}}`

- Elimina tutti i messaggi dalla coda specificata:

`aws sqs purge-queue --queue-url https://sqs.{{regione}}.amazonaws.com/{{nome_coda}}`

- Abilita un account AWS specifico a inviare messaggi alla coda:

`aws sqs add-permission --queue-url https://sqs.{{regione}}.amazonaws.com/{{nome_coda}} --label {{permission_name}} --aws-account-ids {{account_id}} --actions SendMessage`
