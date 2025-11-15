# iptables

> Linux 커널 IPv4 방화벽의 테이블, 체인 및 규칙을 구성합니다.
> IPv6 트래픽 규칙 설정을 위해서는 `ip6tables`를 사용하세요. 같이 보기: `iptables-save`, `iptables-restore`.
> 더 많은 정보: <https://manned.org/iptables>.

- 필터 테이블의 체인, 규칙, 패킷/바이트 카운터 및 라인 번호 보기:

`sudo iptables {{[-vnL --line-numbers|--verbose --numeric --list --line-numbers]}}`

- 체인 [P]규칙 설정:

`sudo iptables {{[-P|--policy]}} {{체인}} {{규칙}}`

- IP에 대한 체인 정책에 규칙 [A]추가:

`sudo iptables {{[-A|--append]}} {{체인}} {{[-s|--source]}} {{IP}} {{[-j|--jump]}} {{규칙}}`

- [p]프로토콜과 포트를 고려하여 IP에 대한 체인 정책에 규칙 [A]추가:

`sudo iptables {{[-A|--append]}} {{체인}} {{[-s|--source]}} {{IP}} {{[-p|--protocol]}} {{tcp|udp|icmp|...}} --dport {{포트}} {{[-j|--jump]}} {{규칙}}`

- `192.168.0.0/24` 서브넷의 모든 트래픽을 호스트의 공인 IP로 변환하는 NAT 규칙 추가:

`sudo iptables {{[-t|--table]}} {{nat}} {{[-A|--append]}} {{POSTROUTING}} {{[-s|--source]}} {{192.168.0.0/24}} {{[-j|--jump]}} {{MASQUERADE}}`

- 체인 규칙 [D]삭제:

`sudo iptables {{[-D|--delete]}} {{체인}} {{규칙_라인_번호}}`
