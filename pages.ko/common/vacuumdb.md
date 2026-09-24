# vacuumdb

> PostgreSQL 데이터베이스에 불필요한 데이터를 정리 및 분석.
> 더 많은 정보: <https://www.postgresql.org/docs/current/app-vacuumdb.html>.

- 지정한 데이터베이스에 불필요한 데이터를 정리 및 분석:

`vacuumdb {{데이터베이스_이름}}`

- 모든 데이터베이스에 불필요한 데이터를 정리 및 분석:

`vacuumdb {{[-a|--all]}}`

- 데이터베이스의 지정한 테이블에 Vacuum 수행:

`vacuumdb {{[-t|--table]}} {{테이블_이름}} {{데이터베이스_이름}}`

- Vacuum 수행 후 쿼리 플래너를 위한 통계 업데이트:

`vacuumdb {{[-z|--analyze]}} {{데이터베이스_이름}}`

- full vacuum 수행 (더 적극적으로 공간 회수, 테이블을 잠그고 전체 테이블을 다시 작성):

`vacuumdb {{[-f|--full]}} {{데이터베이스_이름}}`

- 자세한 출력을 표시하고 Vacuum 수행:

`vacuumdb {{[-v|--verbose]}} {{데이터베이스_이름}}`

- 여러 병렬 작업을 사용하여 데이터베이스에 Vacuum 수행:

`vacuumdb --jobs {{작업_개수}} {{데이터베이스_이름}}`
