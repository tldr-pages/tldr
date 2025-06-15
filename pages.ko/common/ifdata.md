# ifdata

> 네트워크 인터페이스에 대한 정보를 표시.
> 더 많은 정보: <https://manned.org/ifdata>.

- 지정된 인터페이스의 전체 구성을 표시:

`ifdata -p {{eth0}}`

- 종료 코드를 통해 지정된 인터페이스의 존재([e]xistence)를 나타냄:

`ifdata -e {{eth0}}`

- 지정된 인터페이스의 IPv4 주소([a]ddress)와 넷마스크([n]etmask)를 표시:

`ifdata -pa -pn {{eth0}}`

- 네트워크([N]etwork) 주소, 브로드캐스트([b]roadcast) 주소 및 지정된 인터페이스의 MTU를 표시:

`ifdata -pN -pb -pm {{eth0}}`

- 도움말 표시:

`ifdata`
