# clusterdb

> PostgreSQL 데이터베이스를 클러스터링(재구성)).
> 더 많은 정보: <https://www.postgresql.org/docs/current/app-clusterdb.html>.

- 특정 데이터베이스를 클러스터링:

`clusterdb {{데이터베이스_이름}}`

- 모든 데이터베이스를 클러스터링:

`clusterdb {{[-a|--all]}}`

- 데이터베이스 내 특정 테이블을 클러스터링:

`clusterdb {{[-t|--table]}} {{테이블_이름}} {{데이터베이스_이름}}`
