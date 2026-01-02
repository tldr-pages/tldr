# avahi-resolve

> 호스트 이름과 IP 주소 간 변환.
> 더 많은 정보: <https://manned.org/avahi-resolve>.

- 로컬 서비스를 IPv4로 변환:

`avahi-resolve -4 --name {{service.local}}`

- IP를 호스트 이름으로 변환, 자세히:

`avahi-resolve --verbose --address {{IP}}`
