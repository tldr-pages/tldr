# pg_dumpall

> PostgreSQL 데이터베이스 클러스터를 스크립트 파일 또는 다른 아카이브 파일로 추출.
> 더 많은 정보: <https://www.postgresql.org/docs/current/app-pg-dumpall.html>.

- 모든 데이터베이스 덤프:

`pg_dumpall > {{경로/대상/파일.sql}}`

- 특정 사용자 이름을 사용하여 모든 데이터베이스 덤프:

`pg_dumpall {{[-U|--username]}} {{사용자_이름}} > {{경로/대상/파일.sql}}`

- 위와 동일하며, 호스트와 포트 맞춤 설정:

`pg_dumpall {{[-h|--host]}} {{호스트}} {{[-p|--port]}} {{포트}} > {{출력_파일.sql}}`

- 데이터베이스 데이터를 SQL 스크립트 파일로만 덤프:

`pg_dumpall {{[-a|--data-only]}} > {{경로/대상/파일.sql}}`

- 스키마(데이터 정의)만 SQL 스크립트 파일로 덤프:

`pg_dumpall {{[-s|--schema-only]}} > {{출력_파일.sql}}`
