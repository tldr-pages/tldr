# terraform taint

> 리소스 인스턴스를 정상적으로 작동하지 않는 상태로 표시해 다음 apply 실행 시, 강제로 교체되도록 함.
> 참고: 이 명령은 더 이상 권장되지 않음. 대신 `terraform apply -replace`을 사용.
> 관련 항목: `terraform apply`, `terraform untaint`.
> 더 많은 정보: <https://developer.hashicorp.com/terraform/cli/commands/taint>.

- 리소스를 tainted 상태로 표시:

`terraform taint {{리소스_타입.리소스_이름[인스턴스_인덱스]}}`

- 리소스가 존재하지 않더라도, tainted 상태로 표시:

`terraform taint -allow-missing {{리소스_타입.리소스_이름[인스턴스_인덱스]}}`

- 상태 잠금을 획득하지 않고 리소스를 tainted 상태로 표시:

`terraform taint -lock=false {{리소스_타입.리소스_이름[인스턴스_인덱스]}}`

- 잠금 대기 시간을 지정해, 리소스를 tainted 상태로 표시:

`terraform taint -lock-timeout={{시간}} {{리소스_타입.리소스_이름[인스턴스_인덱스]}}`
