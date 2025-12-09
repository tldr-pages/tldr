# k3d

> Docker 내에 k3s 클러스터를 쉽게 생성할 수 있는 래퍼.
> 더 많은 정보: <https://k3d.io/stable/usage/commands/>.

- 클러스터 생성:

`k3d cluster create {{클러스터_이름}}`

- 클러스터 삭제:

`k3d cluster delete {{클러스터_이름}}`

- 새로운 컨테이너화된 k3s 노드 생성:

`k3d node create {{노드_이름}}`

- Docker에서 k3d 클러스터로 이미지 가져오기:

`k3d image import {{이미지_이름}} --cluster {{클러스터_이름}}`

- 새로운 레지스트리 생성:

`k3d registry create {{레지스트리_이름}}`
