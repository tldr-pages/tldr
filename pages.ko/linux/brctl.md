# brctl

> Ethernet 브리지 관리 도구.
> 더 많은 정보: <https://manned.org/brctl>.

- 현재 존재하는 Ethernet 브리지에 대한 정보를 나열:

`sudo brctl show`

- 새 Ethernet 브리지 인터페이스 생성:

`sudo brctl add {{브리지_이름}}`

- 기존 Ethernet 브리지 인터페이스 삭제:

`sudo brctl del {{브리지_이름}}`

- 기존 브리지에 인터페이스 추가:

`sudo brctl addif {{브리지_이름}} {{인터페이스_이름}}`

- 기존 브리지에서 인터페이스 제거:

`sudo brctl delif {{브리지_이름}} {{인터페이스_이름}}`
