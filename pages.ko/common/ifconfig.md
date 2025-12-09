# ifconfig

> 네트워크 인터페이스 구성자.
> 더 많은 정보: <https://net-tools.sourceforge.io/man/ifconfig.8.html>.

- 인터페이스 네트워크 설정 보기:

`ifconfig {{인터페이스_이름}}`

- 비활성화된 인터페이스를 포함하여, 모든 인터페이스의 세부 정보를 표시:

`ifconfig -a`

- 인터페이스 비활성화:

`ifconfig {{인터페이스_이름}} down`

- 인터페이스 활성화:

`ifconfig {{인터페이스_이름}} up`

- 인터페이스에 IP 주소를 할당:

`ifconfig {{인터페이스_이름}} {{ip_주소}}`
