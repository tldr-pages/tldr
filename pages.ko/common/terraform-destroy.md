# terraform destroy

> Terraform 설정으로 관리되는 모든 객체를 삭제.
> 더 많은 정보: <https://developer.hashicorp.com/terraform/cli/commands/destroy>.

- 현재 디렉터리에서 관리되는 모든 인프라 삭제:

`terraform destroy`

- 대화형 승인 없이, 인프라 삭제:

`terraform destroy -auto-approve`

- 지정한 리소스 삭제:

`terraform destroy -target {{리소스_타입.리소스_이름[인스턴스_인덱스]}}`

- 입력 변수 값 지정:

`terraform destroy -var '{{이름1}}={{값1}}' -var '{{이름2}}={{값2}}'`

- 파일에서 입력 변수 값 불러오기:

`terraform destroy -var-file {{경로/대상/파일.tfvars}}`

- 경고 메시지를 간략하게 표시하며 인프라 삭제:

`terraform destroy -compact-warnings`
