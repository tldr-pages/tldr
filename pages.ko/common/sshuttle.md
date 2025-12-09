# sshuttle

> SSH 연결을 통해 트래픽을 터널링하는 투명 프록시 서버.
> 원격 SSH 서버에서는 루트 권한이나 특별한 설정이 필요하지 않지만, 로컬 머신에서는 루트 접근이 요청됩니다.
> 더 많은 정보: <https://manned.org/sshuttle>.

- 원격 SSH 서버를 통해 모든 IPv4 TCP 트래픽 전달:

`sshuttle --remote={{사용자_명}}@{{ssh서버}} {{0.0.0.0/0}}`

- 서버의 기본 DNS 해석기로 모든 DNS 트래픽도 전달:

`sshuttle --dns --remote={{사용자_명}}@{{ssh서버}} {{0.0.0.0/0}}`

- 특정 서브넷으로 향하는 트래픽을 제외한 모든 트래픽 전달:

`sshuttle --remote={{사용자_명}}@{{ssh서버}} {{0.0.0.0/0}} --exclude {{192.168.0.1/24}}`

- tproxy 방법을 사용하여 모든 IPv4 및 IPv6 트래픽 전달:

`sshuttle --method=tproxy --remote={{사용자_명}}@{{ssh서버}} {{0.0.0.0/0}} {{::/0}} --exclude={{내_로컬_ip_주소}} --exclude={{ssh_서버_ip_주소}}`
