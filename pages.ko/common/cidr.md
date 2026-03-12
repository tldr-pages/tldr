# cidr

> IPv4/IPv6 CIDR 네트워크 프리픽스를 계산, 겹침 확인, 설명, 분할 등의 기능으로 관리할 수 있게 해주는 도구.
> 더 많은 정보: <https://github.com/bschaatsbergen/cidr>.

- CIDR 범위를 설명:

`cidr explain {{10.0.0.0/16}}`

- 특정 주소가 CIDR 범위에 포함되는지 확인:

`cidr contains {{10.0.0.0/16}} {{10.0.14.5}}`

- CIDR 범위에 포함된 모든 주소의 개수를 확인:

`cidr count {{10.0.0.0/16}}`

- 두 CIDR 범위가 서로 겹치는지 확인:

`cidr overlaps {{10.0.0.0/16}} {{10.0.14.0/22}}`

- CIDR 범위를 지정한 개수의 네트워크로 분할:

`cidr divide {{10.0.0.0/16}} {{9}}`
