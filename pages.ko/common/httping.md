# httping

> 웹 서버의 대기 시간과 처리량을 측정.
> 더 많은 정보: <https://manned.org/httping>.

- 지정된 URL을 ping:

`httping -g {{주소}}`

- `호스트` 및 `포트`에서 웹 서버를 ping:

`httping -h {{호스트}} -p {{포트}}`

- TLS 연결을 사용하여 `호스트`에서 웹 서버를 ping:

`httping -l -g https://{{호스트}}`

- HTTP 기본 인증을 사용하여 `호스트`에서 웹 서버를 ping:

`httping -g http://{{호스트}} -U {{사용자명}} -P {{비밀번호}}`
