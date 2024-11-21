# aws secretsmanager

> 시크릿 정보 저장, 관리, 검색.
> 더 많은 정보: <https://docs.aws.amazon.com/cli/latest/reference/secretsmanager/>.

- 현재 계정의 시크릿 정보 관리자가 저장한 시크릿 정보를 표시:

`aws secretsmanager list-secrets`

- 모든 시크릿 정보를 표시하되 시크릿 이름 및 ARN만 표시(보기 쉬움):

`aws secretsmanager list-secrets --query 'SecretList[*].{Name: Name, ARN: ARN}'`

- 시크릿 정보 생성:

`aws secretsmanager create-secret --name {{이름}} --description "{{시크릿_정보}}" --secret-string {{시크릿}}`

- 시크릿 정보 삭제 (복구 없이 즉시 삭제하려면 `--force-delete-without-recovery` 추가):

`aws secretsmanager delete-secret --secret-id {{이름|arn}}`

- 시크릿 텍스트를 제외한 시크릿 세부정보 보기:

`aws secretsmanager describe-secret --secret-id {{이름|arn}}`

- 시크릿의 정보 값을 검색 (시크릿의 최신 버전을 얻으려면 `--version-stage` 생략):

`aws secretsmanager get-secret-value --secret-id {{이름|arn}} --version-stage {{시크릿_버전}}`

- Lambda 함수를 사용하여 즉시 시크릿 정보 교체:

`aws secretsmanager rotate-secret --secret-id {{이름|arn}} --rotation-lambda-arn {{lambda_함수_arn}}`

- Lambda 함수를 사용하여 30일마다 자동으로 보안 암호 교체:

`aws secretsmanager rotate-secret --secret-id {{이름|arn}} --rotation-lambda-arn {{lambda_함수_arn}} --rotation-rules AutomaticallyAfterDays={{30}}`
