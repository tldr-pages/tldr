# az account

> Azure 구독 정보를 관리.
> `azure-cli`의 일부 (`az`라고도 함).
> 더 많은 정보: <https://learn.microsoft.com/cli/azure/account>.

- 로그인한 계정의 모든 구독을 나열:

`az account list`

- `구독`을 햔재 활성 구독으로 설정:

`az account set {{[-s|--subscription]}} {{구독_아이디}}`

- 현재 활성 구독이 지원되는 지역을 나열:

`az account list-locations`

- `MS Graph API`와 함께 사용할 액세스 토큰을 인쇄:

`az account get-access-token --resource-type {{ms-graph}}`

- 현재 활성화된 구독의 세부 정보를 특정 형식으로 출력:

`az account show {{[-o|--output]}} {{json|tsv|table|yaml}}`
