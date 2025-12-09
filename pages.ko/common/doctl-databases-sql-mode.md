# doctl databases sql-mode

> MySQL 데이터베이스 클러스터의 전역 SQL 모드를 보고 구성.
> 더 많은 정보: <https://docs.digitalocean.com/reference/doctl/reference/databases/sql-mode/>.

- 액세스 토큰을 사용하여 `doctl databases sql-mode` 명령을 실행:

`doctl databases sql-mode {{명령어}} --access-token {{액세스_토큰}}`

- MySQL 데이터베이스 클러스터의 SQL 모드를 가져옴:

`doctl databases sql-mode get {{데이터베이스_아이디}}`

- MySQL 데이터베이스 클러스터의 SQL 모드를 지정된 모드로 덮어씀:

`doctl databases sql-mode set {{데이터베이스_아이디}} {{sql_모드_1 sql_모드_2 ...}}`
