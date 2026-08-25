# pg_restore

> pg_dump로 생성된 아카이브 파일에서 PostgreSQL 데이터베이스 복원.
> 더 많은 정보: <https://www.postgresql.org/docs/current/app-pgrestore.html>.

- 기존 데이터베이스에 아카이브 복원:

`pg_restore {{[-d|--dbname]}} {{데이터베이스_이름}} {{아카이브_파일.dump}}`

- 위와 동일하며, 사용자 이름 커스터마이즈:

`pg_restore {{[-U|--username]}} {{사용자_이름}} {{[-d|--dbname]}} {{데이터베이스_이름}} {{아카이브_파일.dump}}`

- 위와 동일하며, 호스트 및 포트 커스터마이즈:

`pg_restore {{[-h|--host]}} {{호스트}} {{[-p|--port]}} {{포트}} {{[-d|--dbname]}} {{데이터베이스_이름}} {{아카이브_파일.dump}}`

- 아카이브에 포함된 데이터베이스 객체 목록:

`pg_restore {{[-l|--list]}} {{아카이브_파일.dump}}`

- 데이터베이스 객체를 생성하기 전에 삭제:

`pg_restore {{[-c|--clean]}} {{[-d|--dbname]}} {{데이터베이스_이름}} {{아카이브_파일.dump}}`

- 여러 작업을 사용하여 복원:

`pg_restore {{[-j|--jobs]}} {{2}} {{[-d|--dbname]}} {{데이터베이스_이름}} {{아카이브_파일.dump}}`
