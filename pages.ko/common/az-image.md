# az image

> Azure에서 사용자 지정 가상 머신 이미지를 관리.
> `azure-cli` (`az`라고도 함)의 일부.
> 더 많은 정보: <https://learn.microsoft.com/cli/azure/image>.

- 리소스 그룹 아래에 사용자 정의 이미지를 나열:

`az image list --resource-group {{리소스_그룹}}`

- 관리 디스크 또는 스냅샷에서 사용자 지정 이미지를 생성:

`az image create --resource-group {{리소스_그룹}} --name {{이름}} --os-type {{windows|linux}} --source {{os_디스크_소스}}`

- 사용자 정의 이미지 삭제:

`az image delete --name {{이름}} --resource-group {{리소스_그룹}}`

- 사용자 정의 이미지의 세부정보 표시:

`az image show --name {{이름}} --resource-group {{리소스_그룹}}`

- 사용자 정의 이미지 업데이트:

`az image update --name {{이름}} --resource-group {{리소스_그룹}} --set {{property=value}}`
