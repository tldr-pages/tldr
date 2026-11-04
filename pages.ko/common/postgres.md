# postgres

> PostgreSQL 데이터베이스 서버 실행.
> 더 많은 정보: <https://www.postgresql.org/docs/current/app-postgres.html>.

- 지정한 포트에서 서버 시작 (기본값: 5432):

`postgres -p {{5433}}`

- 런타임 매개변수 설정 (축약형):

`postgres -c {{shared_buffers=128MB}}`

- 런타임 매개변수 설정 (긴 형식):

`postgres --{{shared-buffers}}={{128MB}}`

- 특정 데이터베이스를 단일 사용자 모드로 시작 (기본값은 현재 사용자 이름):

`postgres --single -D {{경로/대상/데이터_디렉토리}} {{자신의_데이터베이스}}`
