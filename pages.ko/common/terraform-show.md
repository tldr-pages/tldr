# terraform show

> Terraform 상태 또는 계획 파일을 읽어 사람이 읽기 쉬운 형식으로 출력.
> 더 많은 정보: <https://developer.hashicorp.com/terraform/cli/commands/show>.

- 현재 상태 표시:

`terraform show`

- 지정한 상태 파일 표시:

`terraform show {{경로/대상/terraform.tfstate}}`

- 지정한 계획 파일 표시:

`terraform show {{경로/대상/파일.tfplan}}`

- JSON 형식으로 출력:

`terraform show -json`

- 계획 파일을 JSON 형식으로 출력:

`terraform show -json {{경로/대상/파일.tfplan}}`

- 색상 코드 없이 결과를 파일에 저장:

`terraform show -no-color > {{경로/대상/파일}}`