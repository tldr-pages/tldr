# arp

> 시스템의 ARP 캐시 표시 및 조작.

- 현재 arp 테이블을 보여줍니다:

`arp -a`

- 전체 캐시 삭제:

`sudo arp -a -d`

- 특정 엔트리 삭제:

`arp -d {{address}}`

- 엔트리 생성:

`arp -s {{address}} {{mac_address}}`
