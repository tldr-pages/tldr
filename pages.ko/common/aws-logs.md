# aws logs

> 다양한 AWS 서비스의 로그 파일과 상호작용.
> 더 많은 정보: <https://docs.aws.amazon.com/cli/latest/reference/logs/>.

- 로그 그룹 목록 표시:

`aws logs list-log-groups`

- CloudWatch 로그 그룹의 로그를 지속적으로 조회:

`aws logs tail {{로그_그룹_이름}} --follow`

- 필터를 기반으로 CloudWatch 로그 그룹의 로그 조회:

`aws logs tail {{로그_그룹_이름}} --filter-pattern {{패턴}}`

- 로그 그룹의 실시간에 가까운 로그를 스트리밍:

`aws logs start-live-tail --log-group-identifiers {{로그_그룹_이름}}`

- 로그를 S3 버킷으로 내보내기:

`aws logs create-export-task --log-group-name {{로그_그룹_이름}} --from {{시작_시간}} --to {{종료_시간}} --destination {{s3_버킷_이름}}`
