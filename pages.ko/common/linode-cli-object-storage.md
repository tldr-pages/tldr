# linode-cli object-storage

> Linode 오브젝트 스토리지 관리.
> 같이 보기: `linode-cli`.
> 더 많은 정보: <https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-object-storage>.

- 모든 오브젝트 스토리지 버킷 나열:

`linode-cli object-storage buckets list`

- 새 오브젝트 스토리지 버킷 생성:

`linode-cli object-storage buckets create --cluster {{클러스터_ID}} --label {{버킷_레이블}}`

- 오브젝트 스토리지 버킷 삭제:

`linode-cli object-storage buckets delete {{클러스터_ID}} {{버킷_레이블}}`

- 오브젝트 스토리지 클러스터 지역 나열:

`linode-cli object-storage clusters list`

- 오브젝트 스토리지의 액세스 키 나열:

`linode-cli object-storage keys list`

- 오브젝트 스토리지에 대한 새 액세스 키 생성:

`linode-cli object-storage keys create --label {{레이블}}`

- 오브젝트 스토리지에 대한 액세스 키 해제:

`linode-cli object-storage keys revoke {{액세스_키_ID}}`
