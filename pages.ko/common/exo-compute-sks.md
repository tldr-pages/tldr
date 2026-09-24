# exo compute sks

> Exoscale Scalable Kubernetes Service (SKS)를 관리.
> 더 많은 정보: <https://community.exoscale.com/product/compute/containers/>.

- 지원되는 SKS 클러스터 버전 목록 조회:

`exo compute sks versions`

- 새로운 SKS 클러스터 생성:

`exo compute sks create {{클러스터_이름}} {{[-z|--zone]}} {{zone}}`

- 모든 SKS 클러스터 목록 조회:

`exo compute sks list`

- 유효기간 1800초의 SKS 클러스터의 Kubernetes kubeconfig 생성:

`exo compute sks kubeconfig {{클러스터_이름_또는_아이디}} {{사용자}} --ttl 1800 {{[-z|--zone]}} {{zone}}`

- 3개의 노드를 가진 Nodepool 생성 및 SKS 클러스터에 추가:

`exo compute sks nodepool add {{클러스터_이름_또는_아이디}} {{nodepool_이름}} --size 3 {{[-z|--zone]}} {{zone}}`

- SKS 클러스터에서 Nodepool 제거:

`exo compute sks nodepool delete {{클러스터_이름_또는_아이디}} {{nodepool_이름_또는_아이디}}`

- SKS 클러스터 내 Nodepool에서 특정 노드 제거:

`exo compute sks nodepool evict {{클러스터_이름_또는_아이디}} {{nodepool_이름_또는_아이디}} {{node_이름_또는_아이디}}`

- 기존 SKS 클러스터에 Exoscale CSI 드라이버 활성화:

`exo compute sks update {{클러스터_이름_또는_아이디}} --enable-csi-addon {{[-z|--zone]}} {{zone}}`
