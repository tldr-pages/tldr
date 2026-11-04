# terraform apply

> Terraform 설정 파일에 따라 인프라를 생성하거나 업데이트.
> 더 많은 정보: <https://developer.hashicorp.com/terraform/cli/commands/apply>.

- 인프라 생성 또는 업데이트:

`terraform apply`

- 대화형 승인 없이, 인프라 생성 또는 업데이트:

`terraform apply -auto-approve`

- 계획 파일 적용:

`terraform apply {{경로/대상/파일.tfplan}}`

- 입력 변수 값 지정:

`terraform apply -var '{{이름1}}={{값1}}' -var '{{이름2}}={{값2}}'`

- 파일에서 입력 변수 값 불러오기:

`terraform apply -var-file {{경로/대상/파일.tfvars}}`

- 지정한 리소스에만 변경 사항 적용:

`terraform apply -target {{리소스_타입.리소스_이름[인스턴스_인덱스]}}`

- 지정한 리소스를 교체:

`terraform apply -replace {{리소스_타입.리소스_이름[인스턴스_인덱스]}}`

- Terraform으로 관리되는 인프라 삭제:

`terraform apply -destroy`
