# terraform untaint

> 리소스 인스턴스의 tainted 상태를 해제.
> 관련 항목: `terraform taint`.
> 더 많은 정보: <https://developer.hashicorp.com/terraform/cli/commands/untaint>.

- 리소스의 tainted 상태 해제:

`terraform untaint {{리소스_타입.리소스_이름[인스턴스_인덱스]}}`

- 리소스가 존재하지 않더라도, tainted 상태 해제:

`terraform untaint -allow-missing {{리소스_타입.리소스_이름[인스턴스_인덱스]}}`

- 상태 잠금을 획득하지 않고 tainted 상태 해제:

`terraform untaint -lock=false {{리소스_타입.리소스_이름[인스턴스_인덱스]}}`

- 잠금 대기 시간을 지정하여 tainted 상태 해제:

`terraform untaint -lock-timeout={{시간}} {{리소스_타입.리소스_이름[인스턴스_인덱스]}}`
