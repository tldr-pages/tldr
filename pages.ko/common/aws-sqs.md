# aws sqs

> AWS SQS 서비스 대기열에 메시지 생성, 삭제 및 전송.
> 더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/index.html>.

- 사용 가능한 모든 대기열 나열:

`aws sqs list-queues`

- 특정 대기열의 URL 표시:

`aws sqs get-queue-url --queue-name {{큐_이름}}`

- JSON 형식의 파일에서 특정 속성을 사용하여 대기열을 생성:

`aws sqs create-queue --queue-name {{큐_이름}} --attributes {{file://경로/대상/속성_파일.json}}`

- 특정 메시지를 대기열로 보냄:

`aws sqs send-message --queue-url https://sqs.{{리전}}.amazonaws.com/{{큐_이름}} --message-body "{{메시지_본문}}" --delay-seconds {{지연}} --message-attributes {{file://경로/대상/속성_파일.json}}`

- 대기열에서 지정된 메시지를 삭제:

`aws sqs delete-message --queue-url {{https://queue_url}} --receipt-handle {{receipt_handle}}`

- 특정 큐 삭제:

`aws sqs delete-queue --queue-url https://sqs.{{리전}}.amazonaws.com/{{큐_이름}}`

- 지정된 대기열에서 모든 메시지를 삭제:

`aws sqs purge-queue --queue-url https://sqs.{{리전}}.amazonaws.com/{{큐_이름}}`

- 대기열에 메시지를 보내려면, 특정 AWS 계정을 활성화:

`aws sqs add-permission --queue-url https://sqs.{{리전}}.amazonaws.com/{{큐_이름}} --label {{권한_이름}} --aws-account-ids {{계정_아이디}} --actions SendMessage`
