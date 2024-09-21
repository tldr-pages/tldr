# az aks

> Azure Kubernetes Service (AKS) 클러스터 관리.
> `azure-cli`의 일부 (`az`라고도 함).
> 더 많은 정보: <https://learn.microsoft.com/cli/azure/aks>.

- AKS 클러스터 나열:

`az aks list --resource-group {{리소스_그룹}}`

- 새로운 AKS 클러스터 생성:

`az aks create --resource-group {{리소스_그룹}} --name {{이름}} --node-count {{개수}} --node-vm-size {{크기}}`

- AKS 클러스터 삭제:

`az aks delete --resource-group {{리소스_그룹}} --name {{이름}}`

- AKS 클러스터에 대한 접근 자격 증명을 가져옴:

`az aks get-credentials --resource-group {{리소스_그룹}} --name {{이름}}`

- AKS 클러스터에 사용할 수 있는 업그레이드 버전 가져오기:

`az aks get-upgrades --resource-group {{리소스_그룹}} --name {{이름}}`
