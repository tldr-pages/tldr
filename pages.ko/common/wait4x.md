# wait4x

> 포트 또는 서비스가 요청한 상태가 될 때까지 기다림 (TCP, HTTP, DNS, 데이터베이스 및 메시지 큐를 지원).
> `tcp`, `http` 등 일부 하위 명령은 각각 별도의 사용 문서를 제공함.
> 더 많은 정보: <https://github.com/wait4x/wait4x>.

- TCP 포트를 사용할 수 있을 때까지 대기:

`wait4x tcp {{localhost:8080}}`

- HTTP 엔드포인트가 지정한 상태 코드를 반환할 때까지 대기:

`wait4x http {{https://example.com/health}} --expect-status-code {{200}}`

- PostgreSQL 데이터베이스가 준비될 때까지 대기:

`wait4x postgresql '{{postgres://user:password@localhost:5432/mydb?sslmode=disable}}'`

- Redis 서버를 사용할 수 있을 때까지 대기:

`wait4x redis {{redis://localhost:6379}}`

- 사용자 지정 타임아웃과 확인 간격을 설정하여 서비스 대기:

`wait4x tcp {{localhost:3306}} --timeout {{30s}} --interval {{2s}}`

- 여러 서비스를 병렬로 대기:

`wait4x tcp {{localhost:3306 localhost:6379 ...}}`

- 하위 명령어의 도움말 표시:

`wait4x {{하위명령어}} --help`

- 버전 정보 표시:

`wait4x version`
