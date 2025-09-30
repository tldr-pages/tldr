# rbac-lookup

> Kubernetes 클러스터에서 사용자, 서비스 계정 또는 그룹 이름에 연결된 역할 및 클러스터 역할을 찾습니다.
> 더 많은 정보: <https://github.com/reactiveops/rbac-lookup>.

- 모든 RBAC 바인딩 보기:

`rbac-lookup`

- 주어진 표현식과 일치하는 RBAC 바인딩 보기:

`rbac-lookup {{검색_어구}}`

- 소스 역할 바인딩과 함께 모든 RBAC 바인딩 보기:

`rbac-lookup -o wide`

- 주체로 필터링된 모든 RBAC 바인딩 보기:

`rbac-lookup -k {{사용자|그룹|서비스계정}}`

- IAM 역할과 함께 모든 RBAC 바인딩 보기 (GKE를 사용하는 경우):

`rbac-lookup --gke`
