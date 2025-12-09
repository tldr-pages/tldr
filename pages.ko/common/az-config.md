# az config

> Azure CLI 구성을 관리.
> `azure-cli`의 일부 (`az`라고도 함).
> 더 많은 정보: <https://learn.microsoft.com/cli/azure/config>.

- 모든 구성 설정을 출력:

`az config get`

- 특정 섹션에 대한 구성 설정 출력:

`az config get {{섹션_이름}}`

- 구성을 설정:

`az config set {{구성_이름}}={{값}}`

- 구성 설정을 해제:

`az config unset {{구성_이름}}`
