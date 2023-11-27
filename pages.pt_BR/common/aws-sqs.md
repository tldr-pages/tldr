# aws sqs

> Cria, apaga, e envia mensagens para filas para o serviço AWS SQS.
> Mais informações: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/index.html>.

- Lista todas as filas disponíveis:

`aws sqs list-queues`

- Exibe a URL de uma fila específica:

`aws sqs get-queue-url --queue-name {{nome_da_fila}}`

- Cria uma fila com atributos especificados em arquivo JSON:

`aws sqs create-queue --queue-name {{nome_da_fila}} --attributes {{file://caminho/para/arquivos_de_atributos.json}}`

- Envia mensagem específica para uma fila:

`aws sqs send-message --queue-url https://sqs.{{regiao}}.amazonaws.com/{{nome_da_fila}} --message-body "{{corpo_da_mensagem}}" --delay-seconds {{inteiro}} --message-attributes {{file://caminho/para/arquivos_de_atributos.json}}`

- Remove uma mensagem específica de uma fila:

`aws sqs delete-message --queue-url {{https://url_da_fila}} --receipt-handle {{identificado_da_mensagem}}`

- Remove uma fila específica:

`aws sqs delete-queue --queue-url https://sqs.{{regiao}}.amazonaws.com/{{nome_da_fila}}`

- Remove todas as mensagens de uma fila específica:

`aws sqs purge-queue --queue-url https://sqs.{{regiao}}.amazonaws.com/{{nome_da_fila}}`

- Habilita uma conta AWS específica para enviar mensagens para uma fila:

`aws sqs add-permission --queue-url https://sqs.{{regiao}}.amazonaws.com/{{nome_da_fila}} --label {{nome_da_permissao}} --aws-account-ids {{id_da_conta}} --actions SendMessage`
