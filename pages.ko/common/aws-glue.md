# aws glue

> AWS Glue용 CLI.
> AWS Glue 서비스에 대한 퍼블릭 엔드포인트 정의.
> 더 많은 정보: <https://docs.aws.amazon.com/cli/latest/reference/glue/>.

- 작업 나열:

`aws glue list-jobs`

- 작업 시작:

`aws glue start-job-run --job-name {{작업_이름}}`

- 워크플로우 실행 시작:

`aws glue start-workflow-run --name {{워크플로우_이름}}`

- 트리거 나열:

`aws glue list-triggers`

- 트리거 시작:

`aws glue start-trigger --name {{트리거_이름}}`

- 개발 엔드포인트 생성:

`aws glue create-dev-endpoint --endpoint-name {{이름}} --role-arn {{role_arn_used_by_endpoint}}`
