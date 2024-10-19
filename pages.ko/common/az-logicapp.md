# az logicapp

> Azure 클라우드 서비스에서 로직 앱 관리.
> `azure-cli`(`az`라고도 함)의 일부.
> 자세한 정보: <https://learn.microsoft.com/cli/azure/logicapp>.

- 로직 앱을 생성:

`az logicapp create --name {{name}} --resource-group {{resource_group}} --storage-account {{storage_account}}`

- 로직 앱을 삭제:

`az logicapp delete --name {{name}} --resource-group {{resource_group}}`

- 로직 앱 나열:

`az logicapp list --resource-group {{resource_group}}`

- 로직 앱을 다시 시작:

`az logicapp restart --name {{name}} --resource-group {{resource_group}}`

- 로직 앱을 시작:

`az logicapp start --name {{name}} --resource-group {{resource_group}}`

- 로직 앱을 중지:

`az logicapp stop --name {{name}} --resource-group {{resource_group}}`
