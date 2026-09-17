# arptables

> `nftables` 백엔드를 사용하여 ARP 필터링 규칙을 관리하는 도구.
> ARP 패킷 필터링을 위한 `xtables-nft` 도구의 일부 .
> 더 많은 정보: <https://manned.org/arptables>.

- filter 테이블의 모든 ARP 규칙 목록 출력:

`sudo arptables {{[-L|--list]}}`

- 특정 IP 주소에서 오는 ARP 패킷을 차단하는 규칙 추가:

`sudo arptables {{[-A|--append]}} INPUT {{[-s|--source-ip]}} {{192.168.0.1}} {{[-j|--jump]}} DROP`

- INPUT 체인에서 규칙 번호를 이용해 특정 규칙 삭제:

`sudo arptables {{[-D|--delete]}} INPUT {{규칙_번호}}`

- filter 테이블의 모든 규칙 삭제:

`sudo arptables {{[-F|--flush]}}`

- OUTPUT 체인의 기본 정책을 ACCEPT로 설정:

`sudo arptables {{[-P|--policy]}} OUTPUT ACCEPT`

- 현재 ARP 규칙을 파일로 저장:

`sudo arptables-save > {{경로/대상/파일}}`
