# terraform output

> Terraform 리소스에 대한 구조화된 데이터를 내보내기.
> 더 많은 정보: <https://developer.hashicorp.com/terraform/cli/commands/output>.

- 추가 인수 없이, `output`은 루트 모듈의 모든 출력을 표시:

`terraform output`

- 특정 이름의 값만 출력:

`terraform output {{이름}}`

- 출력 값을 일반 문자열로 변환 (쉘 스크립트에 유용):

`terraform output -raw`

- 출력을 각 출력별 키가 있는 JSON 객체로 포맷 (jq와 함께 사용 시 유용):

`terraform output -json`
