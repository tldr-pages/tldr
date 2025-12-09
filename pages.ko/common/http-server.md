# http-server

> 정적 파일을 제공하는 간단한 정적 HTTP 서버.
> 더 많은 정보: <https://github.com/http-party/http-server>.

- 현재 디렉터리를 제공하기 위해 기본 포트에서 수신 대기하는 HTTP 서버를 시작:

`http-server`

- 특정 디렉터리를 제공하려면 특정 포트에서 HTTP 서버를 시작:

`http-server {{경로/대상/디렉토리}} --port {{포트}}`

- 기본 인증을 사용하여 HTTP 서버를 시작:

`http-server --username {{사용자명}} --password {{비밀번호}}`

- 디렉토리 목록이 비활성화된 상태에서 HTTP 서버를 시작:

`http-server -d {{false}}`

- 지정된 인증서를 사용하여 기본 포트에서 HTTPS 서버를 시작:

`http-server --ssl --cert {{경로/대상/인증서.pem}} --key {{경로/대상/키.pem}}`

- HTTP 서버를 시작하고 출력 로깅에 클라이언트의 IP 주소를 포함:

`http-server --log-ip`

- 모든 응답에 `Access-Control-Allow-Origin: *` 헤더를 포함하여 CORS가 활성화된 HTTP 서버를 시작:

`http-server --cors`

- 로깅이 비활성화된 상태에서 HTTP 서버를 시작:

`http-server --silent`
