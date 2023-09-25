# aws

> Amazon Web Services의 공식 CLI tool입니다.
> `aws s3`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
> 더 많은 정보: <https://aws.amazon.com/cli>.

- AWS Command-line 설정:

`aws configure wizard`

- SSO를 사용해 AWS Command-line 설정:

`aws configure sso`

- AWS 명령에 대한 도움말:

`aws {{command}} help`

- 호출자 ID 가져오기 (권한 문제 해결에 사용됨):

`aws sts get-caller-identity`

- 지역의 AWS 리소스 목록 및 YAML로 출력:

`aws dynamodb list-tables --region {{us-east-1}} --output yaml`

- 명령에 대한 자동 프롬프트 사용:

`aws iam create-user --cli-auto-prompt`

- AWS 리소스에 대한 대화형 마법사 사용:

`aws dynamodb wizard {{new_table}}`

- JSON CLI 스켈레톤 생성 (인프라를 코드로 사용하는 데 유용):

`aws dynamodb update-table --generate-cli-skeleton`
