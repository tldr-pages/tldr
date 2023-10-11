# arp

> 시스템의 ARP 캐시 표시 및 조작.
> 더 많은 정보: <https://manned.org/arp>.

- 현재 arp 테이블을 보여줍니다:

`arp -a`

- 특정 엔트리 삭제:

`arp -d {{address}}`

- 엔트리 생성:

`arp -s {{address}} {{mac_address}}`
