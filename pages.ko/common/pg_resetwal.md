# pg_resetwal

> PostgreSQL 데이터베이스 클러스터의 write-ahead log 및 제어 정보를 초기화.
> 더 많은 정보: <https://www.postgresql.org/docs/current/app-pgresetwal.html>.

- 지정한 데이터 디렉터리의 WAL 및 제어 정보 초기화:

`pg_resetwal {{[-D|--pgdata]}} {{경로/대상/데이터}}`

- dry run 수행:

`pg_resetwal {{[-D|--pgdata]}} {{경로/대상/데이터}} {{[-n|--dry-run]}}`

- WAL 및 제어 정보 강제 초기화:

`pg_resetwal {{[-D|--pgdata]}} {{경로/대상/데이터}} {{[-f|--force]}}`

- 도움말 표시:

`pg_resetwal {{[-?|--help]}}`

- 버전 정보 표시:

`pg_resetwal {{[-V|--version]}}`
