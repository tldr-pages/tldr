# aws batch

> AWS Batch를 통해 배치 컴퓨팅 워크로드를 실행합니다.
> 더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/index.html>.

- 실행 중인 배치 작업 목록:

`aws batch list-jobs --job-queue {{queue_name}}`

- 컴퓨팅 환경 생성:

`aws batch create-compute-environment --compute-environment-name {{compute_environment_name}} --type {{type}}`

- 배치 작업 큐 생성:

`aws batch create-job-queue --job-queue-name {{queue_name}} --priority {{priority}} --compute-environment-order {{compute_environment}}`

- 작업 제출:

`aws batch submit-job --job-name {{job_name}} --job-queue {{job_queue}} --job-definition {{job_definition}}`

- 배치 작업 목록 설명:

`aws batch describe-jobs --jobs {{jobs}}`

- 작업 취소:

`aws batch cancel-job --job-id {{job_id}} --reason {{reason}}`
