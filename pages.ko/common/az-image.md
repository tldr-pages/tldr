# az image

> Azure에서 사용자 지정 가상 머신 이미지를 관리.
> `azure-cli`(`az`라고도 함)의 일부.
> 자세한 정보: <https://learn.microsoft.com/cli/azure/image>.

- 리소스 그룹 아래에 사용자 지정 이미지를 나열:

`az image list --resource-group {{resource_group}}`

- 관리 디스크 또는 스냅샷에서 사용자 지정 이미지를 생성:

`az image create --resource-group {{resource_group}} --name {{name}} --os-type {{windows|linux}} --source {{os_disk_source}}`

- 사용자 지정 이미지를 삭제:
`az image delete --name {{name}} --resource-group {{resource_group}}`

- 사용자 정의 이미지의 세부 정보를 표시:

`az image show --name {{name}} --resource-group {{resource_group}}`

- 사용자 정의 이미지를 업데이트:

`az image update --name {{name}} --resource-group {{resource_group}} --set {{property=value}}`
