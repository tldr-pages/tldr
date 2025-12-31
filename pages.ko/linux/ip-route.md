# ip route

> IP 라우팅 테이블 관리 하위 명령.
> 더 많은 정보: <https://manned.org/ip-route>.

- 라우팅 테이블 표시:

`ip {{[r|route]}}`

- 게이트웨이 포워딩을 사용하여 기본 라우트 추가:

`sudo ip {{[r|route]}} {{[a|add]}} default via {{게이트웨이_IP}}`

- `eth0`을 사용하여 기본 라우트 추가:

`sudo ip {{[r|route]}} {{[a|add]}} default dev {{eth0}}`

- 고정 라우트 추가:

`sudo ip {{[r|route]}} {{[a|add]}} {{대상_IP}} via {{게이트웨이_IP}} dev {{eth0}}`

- 고정 라우트 삭제:

`sudo ip {{[r|route]}} {{[d|delete]}} {{대상_IP}} dev {{eth0}}`

- 고정 라우트 변경 또는 대체:

`sudo ip {{[r|route]}} {{change|replace}} {{대상_IP}} via {{게이트웨이_IP}} dev {{eth0}}`

- 특정 IP 주소에 도달하기 위해 커널이 사용할 라우트 표시:

`ip {{[r|route]}} {{[g|get]}} {{대상_IP}}`
