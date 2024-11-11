# linode-cli lke

> Linode Kubernetes Engine (LKE) 클러스터 관리.
> 같이 보기: `linode-cli`.
> 더 많은 정보: <https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-lke>.

- 모든 LKE 클러스터 나열:

`linode-cli lke clusters list`

- 새 LKE 클러스터 생성:

`linode-cli lke clusters create --region {{지역}} --type {{유형}} --node-type {{노드_유형}} --nodes-count {{수량}}`

- 특정 LKE 클러스터 세부정보 보기:

`linode-cli lke clusters view {{클러스터_ID}}`

- 기존 LKE 클러스터 업데이트:

`linode-cli lke clusters update {{클러스터_ID}} --node-type {{새_노드_유형}}`

- LKE 클러스터 삭제:

`linode-cli lke clusters delete {{클러스터_ID}}`
