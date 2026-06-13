# route

> route 명령어를 사용하여 라우팅 테이블 설정.
> 더 많은 정보: <https://manned.org/route>.

- 라우팅 테이블의 정보를 표시:

`route -n`

- 라우팅 규칙 추가:

`sudo route add -net {{아이피_주소}} netmask {{넷마스크_주소}} gw {{게이트웨이_주소}}`

- 라우팅 규칙 삭제:

`sudo route del -net {{아이피_주소}} netmask {{넷마스크_주소}} dev {{게이트웨이_주소}}`
