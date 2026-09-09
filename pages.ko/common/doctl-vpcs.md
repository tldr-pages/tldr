# doctl vpcs

> DigitalOcean VPC 네트워크를 관리.
> 더 많은 정보: <https://docs.digitalocean.com/reference/doctl/reference/vpcs/>.

- VPC 네트워크 목록 표시:

`doctl vpcs list`

- 이름, 리전 및 IP 범위를 지정하여 VPC 네트워크 생성:

`doctl vpcs create --name {{vpc_이름}} --region {{nyc1}} --ip-range {{10.116.0.0/20}}`

- 지정한 VPC 네트워크의 상세 정보 조회:

`doctl vpcs get {{vpc_아이디}}`

- 지정한 VPC 네트워크의 이름 변경:

`doctl vpcs update {{vpc_아이디}} --name {{새로운_이름}}`

- VPC 네트워크 삭제:

`doctl vpcs delete {{vpc_아이디}}`
