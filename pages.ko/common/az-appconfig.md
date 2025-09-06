# az appconfig

> Azure에서 앱 구성을 관리.
> `azure-cli`의 일부 (`az`라고도 함).
> 더 많은 정보: <https://learn.microsoft.com/cli/azure/appconfig>.

- 앱 구성 만들기:

`az appconfig create --name {{이름}} --resource-group {{그룹_이름}} --location {{위치}}`

- 특정 앱 구성 삭제:

`az appconfig delete --resource-group {{리소스그룹_이름}} --name {{앱구성파일_이름}}`

- 현재 구독 아래의 모든 앱 구성을 나열:

`az appconfig list`

- 특정 리소스 그룹 아래 모든 앱 구성을 나열:

`az appconfig list --resource-group {{리소스그룹_이름}}`

- 앱 구성의 속성 표시:

`az appconfig show --name {{앱구성파일_이름}}`

- 특정 앱 구성 업데이트:

`az appconfig update --resource-group {{리소스그룹_이름}} --name {{앱구성파일_이름}}`
