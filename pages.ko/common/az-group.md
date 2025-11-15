# az group

> 리소스 그룹 및 템플릿 배포를 관리.
> `azure-cli`의 일부 (`az`라고도 함).
> 더 많은 정보: <https://learn.microsoft.com/cli/azure/group>.

- 새로운 리소스 그룹 생성:

`az group create --name {{이름}} --location {{위치}}`

- 리소스 그룹이 있는지 확인:

`az group exists --name {{이름}}`

- 리소스 그룹 삭제:

`az group delete --name {{이름}}`

- 리소스 그룹의 조건이 충족될 때까지 기다림:

`az group wait --name {{이름}} --{{created|deleted|exists|updated}}`
