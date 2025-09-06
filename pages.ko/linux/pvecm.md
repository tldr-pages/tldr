# pvecm

> Proxmox VE 클러스터 관리자.
> 더 많은 정보: <https://pve.proxmox.com/pve-docs/pvecm.1.html>.

- 현재 노드를 기존 클러스터에 추가:

`pvecm add {{호스트명_또는_IP}}`

- 클러스터 구성에 노드 추가 (내부 사용):

`pvecm addnode {{노드}}`

- 이 노드에서 사용 가능한 클러스터 가입 API 버전 표시:

`pvecm apiver`

- 새 클러스터 구성 생성:

`pvecm create {{클러스터명}}`

- 클러스터 구성에서 노드 제거:

`pvecm delnode {{노드}}`

- 클러스터 노드에 대한 로컬 보기 표시:

`pvecm nodes`

- 클러스터 상태에 대한 로컬 보기 표시:

`pvecm status`
