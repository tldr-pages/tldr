# az advisor

> Azure 구독 정보를 관리.
> `azure-cli`의 일부 (`az`라고도 함).
> 더 많은 정보: <https://learn.microsoft.com/cli/azure/advisor>.

- 전체 구독에 대한 Azure Advisor 구성을 나열:

`az advisor configuration list`

- 지정된 구독 또는 리소스 그룹에 대한 Azure Advisor 구성을 표시:

`az advisor configuration show --resource_group {{리소스_그룹}}`

- Azure Advisor 권장사항 나열:

`az advisor recommendation list`

- Azure Advisor 권장사항 활성화:

`az advisor recommendation enable --resource_group {{리소스_그룹}}`

- Azure Advisor 권장사항 비활성화:

`az advisor recommendation disable --resource_group {{리소스_그룹}}`
