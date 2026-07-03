# pg_checksums

> PostgreSQL 데이터베이스 클러스터의 데이터 체크섬을 활성화, 비활성화하거나 검사.
> 더 많은 정보: <https://www.postgresql.org/docs/current/app-pgchecksums.html>.

- 데이터베이스 클러스터의 데이터 체크섬 검사:

`pg_checksums {{[-D|--pgdata]}} {{경로/대상/데이터}}`

- 데이터베이스 클러스터의 데이터 체크섬 활성화:

`pg_checksums {{[-e|--enable]}} {{[-D|--pgdata]}} {{경로/대상/데이터}}`

- 데이터베이스 클러스터의 데이터 체크섬 비활성화:

`pg_checksums {{[-d|--disable]}} {{[-D|--pgdata]}} {{경로/대상/데이터}}`

- 자세한 출력과 함께 데이터 체크섬 검사:

`pg_checksums {{[-v|--verbose]}} {{[-D|--pgdata]}} {{경로/대상/데이터}}`

- 진행 상황을 표시하며 데이터 체크섬 검사:

`pg_checksums {{[-P|--progress]}} {{[-D|--pgdata]}} {{경로/대상/데이터}}`

- 도움말 표시:

`pg_checksums {{[-?|--help]}}`
