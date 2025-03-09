# ip neighbour

> Neighbour/ARP 테이블 관리 IP 하위 명령어.
> 더 많은 정보: <https://manned.org/ip-neighbour.8>.

- Neighbour/ARP 테이블 항목 표시:

`ip {{[n|neighbour]}}`

- `eth0` 장치에서 neighbour 테이블의 항목 제거:

`sudo ip {{[n|neighbour]}} {{[f|flush]}} dev {{eth0}}`

- Neighbour 조회를 수행하고 neighbour 항목 반환:

`ip {{[n|neighbour]}} {{[g|get]}} {{조회_아이피}} dev {{eth0}}`

- Neighbour IP 주소에 대한 ARP 항목을 `eth0`에 추가하거나 삭제:

`sudo ip {{[n|neighbour]}} {{add|delete}} {{아이피_주소}} lladdr {{맥_주소}} dev {{eth0}} nud reachable`

- Neighbour IP 주소에 대한 ARP 항목을 `eth0`에 변경하거나 대체:

`sudo ip {{[n|neighbour]}} {{change|replace}} {{아이피_주소}} lladdr {{새로운_맥_주소}} dev {{eth0}}`
