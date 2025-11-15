# aws kendra

> AWS Kendra의 CLI.
> 더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/index.html>.

- 인덱스 생성:

`aws kendra create-index --name {{이름}} --role-arn {{role_arn}}`

- 인덱스 나열:

`aws kendra list-indexes`

- 인덱스 표시:

`aws kendra describe-index --id {{index_id}}`

- 데이터 소스 나열:

`aws kendra list-data-sources`

- 데이터 소스 정보 표시:

`aws kendra describe-data-source --id {{데이터_소스_아이디}}`

- 검색 쿼리 나열:

`aws kendra list-query-suggestions --index-id {{인덱스_아이디}} --query-text {{쿼리_문자열}}`
