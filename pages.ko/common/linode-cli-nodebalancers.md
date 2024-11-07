# linode-cli nodebalancers

> Linode NodeBalancer 관리.
> 같이 보기: `linode-cli`.
> 더 많은 정보: <https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-nodebalancers>.

- 모든 NodeBalancer 나열:

`linode-cli nodebalancers list`

- 새 NodeBalancer 생성:

`linode-cli nodebalancers create --region {{지역}}`

- 특정 NodeBalancer의 세부 정보 보기:

`linode-cli nodebalancers view {{nodebalancer_id}}`

- 기존 NodeBalancer 업데이트:

`linode-cli nodebalancers update {{nodebalancer_id}} --label {{새_라벨}}`

- NodeBalancer 삭제:

`linode-cli nodebalancers delete {{nodebalancer_id}}`

- NodeBalancer의 구성 목록 나열:

`linode-cli nodebalancers configs list {{nodebalancer_id}}`

- NodeBalancer에 새 구성 추가:

`linode-cli nodebalancers configs create {{nodebalancer_id}} --port {{포트}} --protocol {{프로토콜}}`
