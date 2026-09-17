# pg_verifybackup

> PostgreSQL 클러스터의 베이스 백업 무결성을 검증.
> 더 많은 정보: <https://www.postgresql.org/docs/current/app-pgverifybackup.html>.

- Verify a backup stored in a specific directory:

`pg_verifybackup {{경로/대상/백업}}`

- 진행 상황을 표시하며 백업 검증:

`pg_verifybackup {{[-P|--progress]}} {{경로/대상/백업}}`

- 첫 번째 오류가 발생하면 즉시 종료하며 백업 검증:

`pg_verifybackup {{[-e|--exit-on-error]}} {{경로/대상/백업}}`

- 지정한 파일 또는 디렉터리를 무시하고 백업 검증:

`pg_verifybackup {{[-i|--ignore]}} {{경로/대상/파일_또는_디렉터리}} {{경로/대상/백업}}`

- 다른 위치의 manifest 파일을 사용하여 백업 검증:

`pg_verifybackup {{[-m|--manifest-path]}} {{경로/대상/백업_manifest}} {{경로/대상/백업}}`

- 도움말 표시:

`pg_verifybackup {{[-?|--help]}}`
