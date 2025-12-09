# aws secretsmanager

> 시크릿을 저장, 관리 및 검색.
> 더 많은 정보: <https://docs.aws.amazon.com/cli/latest/reference/secretsmanager/>.

- 현재 계정에 저장된 시크릿 표시:

`aws secretsmanager list-secrets`

- 모든 시크릿 표시 (시크릿 이름 및 ARN만 표시, 보기 쉬움):

`aws secretsmanager list-secrets --query 'SecretList[*].{Name: Name, ARN: ARN}'`

- 시크릿 생성:

`aws secretsmanager create-secret --name {{이름}} --description "{{시크릿_설명}}" --secret-string '{{시크릿}}'`

- 시크릿 삭제 (복구 없이 즉시 삭제하려면 `--force-delete-without-recovery` 추가):

`aws secretsmanager delete-secret --secret-id {{이름|arn}}`

- 시크릿 세부 정보 표시 (시크릿 텍스트 제외):

`aws secretsmanager describe-secret --secret-id {{이름|arn}}`

- 시크릿 값 검색 (최신 버전의 시크릿을 얻으려면 `--version-stage` 생략):

`aws secretsmanager get-secret-value --secret-id {{이름|arn}} --version-stage {{시크릿_버전}}`

- 즉시 시크릿 교체을 위해 람다 함수 사용:

`aws secretsmanager rotate-secret --secret-id {{이름|arn}} --rotation-lambda-arn {{람다_함수_arn}}`

- 30일마다 자동으로 시크릿 교체을 위해 람다 함수 사용:

`aws secretsmanager rotate-secret --secret-id {{이름|arn}} --rotation-lambda-arn {{람다_함수_arn}} --rotation-rules AutomaticallyAfterDays={{30}}`
