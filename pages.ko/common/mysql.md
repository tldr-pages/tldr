# mysql

> MySQL 명령줄 도구.
> 더 많은 정보: <https://manned.org/mysql>.

- 데이터베이스에 연결:

`mysql {{데이터베이스_이름}}`

- 데이터베이스에 연결하고, 비밀번호 입력 요청:

`mysql {{[-u|--user]}} {{사용자}} {{[-p|--password]}} {{데이터베이스_이름}}`

- 다른 호스트의 데이터베이스에 연결:

`mysql {{[-h|--host]}} {{데이터베이스_호스트}} {{데이터베이스_이름}}`

- Unix 소켓을 통해 데이터베이스에 연결:

`mysql {{[-S|--socket]}} {{경로/대상/socket.sock}}`

- 스크립트 파일(배치 파일)에서 SQL 문 실행:

`mysql {{[-e|--execute]}} "source {{파일이름.sql}}" {{데이터베이스_이름}}`

- `mysqldump`로 생성된 백업에서 데이터베이스 복원 (비밀번호 입력 요청):

`mysql {{[-u|--user]}} {{사용자}} {{[-p|--password]}} {{데이터베이스_이름}} < {{경로/대상/backup.sql}}`

- 백업에서 모든 데이터베이스 복원 (비밀번호 입력 요청):

`mysql {{[-u|--user]}} {{사용자}} {{[-p|--password]}} < {{경로/대상/backup.sql}}`
