# az logicapp

> Azure Cloud Services에서 논리 앱을 관리.
> `azure-cli` (`az`라고도 함)의 일부.
> 더 많은 정보: <https://learn.microsoft.com/cli/azure/logicapp>.

- 논리 앱 만들기:

`az logicapp create --name {{이름}} --resource-group {{리소스_그룹}} --storage-account {{스토리지_계정}}`

- 논리 앱 삭제:

`az logicapp delete --name {{이름}} --resource-group {{리소스_그룹}}`

- 논리 앱 나열:

`az logicapp list --resource-group {{리소스_그룹}}`

- 논리 앱을 다시 시작:

`az logicapp restart --name {{이름}} --resource-group {{리소스_그룹}}`

- 논리 앱을 시작:

`az logicapp start --name {{이름}} --resource-group {{리소스_그룹}}`

- 논리 앱을 중지:

`az logicapp stop --name {{이름}} --resource-group {{리소스_그룹}}`
