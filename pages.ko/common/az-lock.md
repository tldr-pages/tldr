# az lock

> Azure 잠금 관리.
> `azure-cli`의 일부 (`az`라고도 함).
> 더 많은 정보: <https://learn.microsoft.com/cli/azure/lock>.

- 읽기 전용 구독 수준의 잠금을 생성:

`az lock create --name {{잠금_이름}} --lock-type ReadOnly`

- 읽기 전용 리소스 그룹 수준 잠금을 생성:

`az lock create --name {{잠금_이름}} --resource-group {{그룹_이름}} --lock-type ReadOnly`

- 구독 수준 잠금을 해제:

`az lock delete --name {{잠금_이름}}`

- 리소스 그룹 수준의 잠금을 삭제:

`az lock delete --name {{잠금_이름}} --resource-group {{그룹_이름}}`

- 구독 수준의 모든 잠금을 나열:

`az lock list`

- 특정 이름([n])으로 구독 수준 잠금 표시:

`az lock show -n {{잠금_이름}}`
