# squid

> 프록시 서버를 통해 HTTP 요청을 캐시하고 전달.
> 더 많은 정보: <https://manned.org/squid>.

- Squid를 백그라운드에서 시작:

`sudo squid`

- Squid를 포그라운드에서 시작:

`sudo squid -N`

- 지정한 설정 파일을 사용하여 Squid 시작:

`sudo squid -f {{경로/대상/squid.conf}}`

- 설정 파일에 오류가 있는지 검사:

`sudo squid -k parse`

- 설정 파일 다시 불러오기:

`sudo squid -k reconfigure`

- Squid를 정상적으로 종료:

`sudo squid -k shutdown`

- 로그 파일 로테이션 수행:

`sudo squid -k rotate`
