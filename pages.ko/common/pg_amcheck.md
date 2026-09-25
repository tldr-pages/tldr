# pg_amcheck

> 하나 이상의 PostgreSQL 데이터베이스에서 손상 여부를 검사.
> 더 많은 정보: <https://www.postgresql.org/docs/current/app-pgamcheck.html>.

- 특정 데이터베이스 검사:

`pg_amcheck {{데이터베이스_이름}}`

- 모든 데이터베이스 검사:

`pg_amcheck {{[-a|--all]}}`

- 지정한 패턴과 일치하는 데이터베이스 검사:

`pg_amcheck {{[-d|--database]}} {{패턴}}`

- 데이터베이스 내 특정 테이블 검사:

`pg_amcheck {{[-t|--table]}} {{패턴}} {{dbname}}`

- 데이터베이스 내 특정 스키마 검사:

`pg_amcheck {{[-s|--schema]}} {{패턴}} {{dbname}}`

- 도움말 표시:

`pg_amcheck {{[-?|--help]}}`
