# pg_dump

> PostgreSQL 데이터베이스를 스크립트 파일 또는 다른 아카이브 파일로 추출.
> 더 많은 정보: <https://www.postgresql.org/docs/current/app-pgdump.html>.

- 데이터베이스를 SQL 스크립트 파일로 덤프:

`pg_dump {{DB_이름}} > {{출력_파일.sql}}`

- 위와 동일하게, 사용자 이름을 지정:

`pg_dump {{[-U|--username]}} {{사용자명}} {{DB_이름}} > {{출력_파일.sql}}`

- 위와 동일하게, 호스트 및 포트를 지정:

`pg_dump {{[-h|--host]}} {{호스트}} {{[-p|--port]}} {{포트}} {{DB_이름}} > {{출력_파일.sql}}`

- 데이터베이스를 사용자 정의 형식의 아카이브 파일로 덤프:

`pg_dump {{[-F|--format]}} {{[c|custom]}} {{DB_이름}} > {{출력_파일.dump}}`

- 데이터베이스 데이터만 SQL 스크립트 파일로 덤프:

`pg_dump {{[-a|--data-only]}} {{DB_이름}} > {{경로/대상/출력_파일.sql}}`

- 스키마(데이터 정의)만 SQL 스크립트 파일로 덤프:

`pg_dump {{[-s|--schema-only]}} {{DB_이름}} > {{경로/대상/출력_파일.sql}}`
