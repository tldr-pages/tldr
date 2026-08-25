# pg_waldump

> PostgreSQL 데이터베이스 클러스터의 write-ahead log (WAL)을 사람이 읽기 쉬운 형태로 출력.
> 더 많은 정보: <https://www.postgresql.org/docs/current/pgwaldump.html>.

- 지정한 WAL 세그먼트의 레코드 표시:

`pg_waldump {{시작_세그먼트}}`

- 두 WAL 세그먼트 사이의 레코드 표시:

`pg_waldump {{시작_세그먼트}} {{종료_세그먼트}}`

- Specify the WAL 파일 디렉터리 지정:

`pg_waldump {{시작_세그먼트}} {{종료_세그먼트}} {{[-p|--path]}} {{path}}`

- 새로 생성되는 WAL 항목을 실시간으로 계속 표시:

`pg_waldump {{시작_세그먼트}} {{종료_세그먼트}} {{[-f|--follow]}}`

- 표시할 레코드 수 제한:

`pg_waldump {{시작_세그먼트}} {{종료_세그먼트}} {{[-n|--limit]}} {{수}}`

- 개별 레코드 대신 요약 통계 표시:

`pg_waldump {{시작_세그먼트}} {{종료_세그먼트}} {{[-z|--stats]}}`

- 특정 리소스 관리자 기준으로 필터링:

`pg_waldump {{시작_세그먼트}} {{종료_세그먼트}} {{[-r|--rmgr]}} {{리소스_관리자_이름}}`

- 도움말 표시:

`pg_waldump {{[-?|--help]}}`
