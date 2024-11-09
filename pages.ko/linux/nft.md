# nft

> Linux 커널 방화벽이 제공하는 테이블, 체인 및 규칙을 구성합니다.
> Nftables는 iptables를 대체합니다.
> 더 많은 정보: <https://wiki.nftables.org/wiki-nftables/index.php/Main_Page>.

- 현재 구성 보기:

`sudo nft list ruleset`

- "inet" 가족과 "filter" 테이블로 새 테이블 추가:

`sudo nft add table {{inet}} {{filter}}`

- 모든 수신 트래픽을 허용하는 새 체인 추가:

`sudo nft add chain {{inet}} {{filter}} {{input}} \{ type {{filter}} hook {{input}} priority {{0}} \; policy {{accept}} \}`

- 여러 TCP 포트를 허용하는 새 규칙 추가:

`sudo nft add rule {{inet}} {{filter}} {{input}} {{tcp}} {{dport \{ telnet, ssh, http, https \} accept}}`

- `192.168.0.0/24` 서브넷의 모든 트래픽을 호스트의 공용 IP로 변환하는 NAT 규칙 추가:

`sudo nft add rule {{nat}} {{postrouting}} ip saddr {{192.168.0.0/24}} {{masquerade}}`

- 규칙 핸들 표시:

`sudo nft --handle --numeric list chain {{family}} {{table}} {{chain}}`

- 규칙 삭제:

`sudo nft delete rule {{inet}} {{filter}} {{input}} handle {{3}}`

- 현재 구성 저장:

`sudo nft list ruleset > {{/etc/nftables.conf}}`
