# doctl

> DigitalOcean 리소스를 관리.
> 더 많은 정보: <https://docs.digitalocean.com/reference/doctl/>.

- DigitalOcean 인증:

`doctl auth init`

- 계정 정보 표시:

`doctl account get`

- 새로운 Droplet:

`doctl compute droplet create {{이름}} --size {{크기}} --image {{이미지}} --region {{리전}}`

- 모든 Droplets 목록 표시:

`doctl compute droplet list`

- Droplet에 SSH 접속:

`doctl compute ssh {{droplet_아이디}}`

- Kubernetes 클러스터 생성:

`doctl kubernetes cluster create {{클러스터_이름}}`

- Kubernetes 클러스터 목록 표시:

`doctl kubernetes cluster list`

- 관리형 데이터베이스 목록 표시:

`doctl databases list`
