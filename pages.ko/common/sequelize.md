# sequelize

> Postgres, MySQL, MariaDB, SQLite 및 Microsoft SQL Server를 위한 Promise 기반 Node.js ORM.
> 더 많은 정보: <https://sequelize.org/docs/v7/cli/>.

- 3개의 필드와 마이그레이션 파일로 모델 생성:

`sequelize model:generate --name {{테이블_이름}} --attributes {{field1:integer,field2:string,field3:boolean}}`

- 마이그레이션 파일 실행:

`sequelize db:migrate`

- 모든 마이그레이션 되돌리기:

`sequelize db:migrate:undo:all`

- 데이터베이스를 채우기 위해 지정된 이름의 시드 파일 생성:

`sequelize seed:generate --name {{시드_파일_이름}}`

- 모든 시드 파일을 사용하여 데이터베이스 채우기:

`sequelize db:seed:all`
