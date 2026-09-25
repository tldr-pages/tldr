# pg_rewind

> PostgreSQL 데이터 디렉토리를 동일한 기반에서 분기된 다른 데이터 디렉토리와 동기화.
> 더 많은 정보: <https://www.postgresql.org/docs/current/app-pgrewind.html>.

- 대상 데이터 디렉토리를 원본 데이터 디렉토리와 동기화:

`pg_rewind {{[-D|--target-pgdata]}} {{경로/대상/대상_데이터}} --source-pgdata {{경로/대상/원본_데이터}}`

- 연결 문자열을 사용하여 원본 서버와 대상 데이터 디렉터리를 동기화 :

`pg_rewind {{[-D|--target-pgdata]}} {{경로/대상/대상_데이터}} --source-server {{connstr}}`

- dry run 실행:

`pg_rewind {{[-D|--target-pgdata]}} {{경로/대상/대상_데이터}} --source-pgdata {{경로/대상/원본_데이터}} {{[-n|--dry-run]}}`

- 진행 상황을 표시하며 동기화:

`pg_rewind {{[-D|--target-pgdata]}} {{경로/대상/대상_데이터}} --source-pgdata {{경로/대상/원본_데이터}} {{[-P|--progress]}}`

- 도움말 표시:

`pg_rewind {{[-?|--help]}}`
