# terraform validate

> 디렉터리 Terraform 설정 파일이 유효한지 검사.
> 더 많은 정보: <https://developer.hashicorp.com/terraform/cli/commands/validate>.

- 현재 디렉터리의 설정 유효성 검사:

`terraform validate`

- 유효성 검사 결과를 JSON 형식으로 출력:

`terraform validate -json`

- 테스트 파일을 제외하고 설정 유효성 검사:

`terraform validate -no-tests`

- 지정한 디렉터리의 설정 유효성 검사:

`terraform validate {{경로/대상/디렉터리}}`

- 사용자 지정 테스트 디렉터리를 사용하여 설정 유효성 검사:

`terraform validate -test-directory {{경로/대상/테스트_디렉터리}}`
