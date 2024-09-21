# az vm

> Azure에서 가상 머신을 관리.
> `azure-cli`의 일부 (`az`라고도 함).
> 더 많은 정보: <https://learn.microsoft.com/cli/azure/vm>.

- 사용 가능한 가상 머신의 세부 정보 나열:

`az vm list`

- 기본 Ubuntu 이미지를 사용하여 가상 머신을 생성하고 SSH 키를 생성:

`az vm create --resource-group {{리소스그룹}} --name {{가상머신_이름}} --image {{UbuntuLTS}} --admin-user {{azureuser}} --generate-ssh-keys`

- 가상 머신 정지:

`az vm stop --resource-group {{리소스그룹}} --name {{가상머신_이름}}`

- 가상 머신 할당 해제:

`az vm deallocate --resource-group {{리소스그룹}} --name {{가상머신_이름}}`

- 가상 머신 시작:

`az vm start --resource-group {{리소스그룹}} --name {{vm_name}}`

- 가상 머신 재시작:

`az vm restart --resource-group {{리소스그룹}} --name {{가상머신_이름}}`

- Azure Marketplace에서 사용할 수 있는 VM 이미지를 나열:

`az vm image list`
