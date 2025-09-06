# az provider

> 리소스 공급자 관리.
> `azure-cli`의 일부 (`az`라고도 함).
> 더 많은 정보: <https://learn.microsoft.com/cli/azure/provider>.

- 공급자 등록:

`az provider register --namespace {{Microsoft.PolicyInsights}}`

- 공급자 등록 취소:

`az provider unregister --namespace {{Microsoft.Automation}}`

- 구독에 대한 모든 공급자를 나열:

`az provider list`

- 특정 공급업체에 대한 정보를 표시:

`az provider show --namespace {{Microsoft.Storage}}`

- 특정 공급자에 대한 모든 리소스 유형을 나열:

`az provider list --query "[?namespace=='{{Microsoft.Network}}'].resourceTypes[].resourceType"`
