# createdb

> PostgreSQL 데이터베이스 생성.
> 더 많은 정보: <https://www.postgresql.org/docs/current/app-createdb.html>.

- 현재 사용자가 가지고 있는 데이터베이스를 생성:

`createdb {{데이터베이스_이름}}`

- 설명과 함께 특정 사용자가 소유한 데이터베이스를 생성:

`createdb --owner {{사용자명}} {{데이터베이스_이름}} '{{설명}}'`

- 템플릿에서 데이터베이스를 생성:

`createdb --template {{템플릿_이름}} {{데이터베이스_이름}}`
