# aws cur

> AWS 사용 보고서 정의 파일 생성, 쿼리 및 삭제.
> 더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cur/index.html>.

- JSON 파일에서 AWS 비용 및 사용 보고서 정의 파일 생성:

`aws cur put-report-definition --report-definition file://{{경로/대상/리포트_정의파일.json}}`

- 로그인 한 계정에 대해 정의된 사용 보고서 정의 나열:

`aws cur describe-report-definitions`

- 사용 보고서 정의 삭제:

`aws cur --region {{aws_리전}} delete-report-definition --report-name {{레포트}}`
