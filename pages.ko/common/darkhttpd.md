# darkhttpd

> Darkhttpd 웹 서버.
> 더 많은 정보: <https://github.com/emikulic/darkhttpd#how-to-run-darkhttpd>.

- 지정된 문서 경로를 제공하는 서버 시작:

`darkhttpd {{경로/문서}}`

- 지정된 포트에서 서버 시작(루트가 아닌 사용자로 시작되는 경우 8080포트가 기본값):

`darkhttpd {{경로/문서}} --port {{포트번호}}`

- 지정된 IP 주소에서만 수신 (기본적으로 서버는 모든 인터페이스에서 수신):

`darkhttpd {{경로/문서}} --addr {{ip주소}}`
