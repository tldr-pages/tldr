# doctl databases

> MySQL, Redis, PostgreSQL 및 MongoDB 데이터베이스 서비스를 관리.
> 더 많은 정보: <https://docs.digitalocean.com/reference/doctl/reference/databases/>.

- 액세스 토큰을 사용하여 `doctl databases` 명령을 실행:

`doctl {{[d|databases]}} {{명령어}} {{[-t|--access-token]}} {{액세스_토큰}}`

- 데이터베이스 클러스터에 대한 세부 정보를 가져옴:

`doctl {{[d|databases]}} {{[g|get]}}`

- 데이터베이스 클러스터를 나열:

`doctl {{[d|databases]}} {{[ls|list]}}`

- 데이터베이스 클러스터 생성:

`doctl {{[d|databases]}} {{[c|create]}} {{데이터베이스_이름}}`

- 클러스터 삭제:

`doctl {{[d|databases]}} {{[rm|delete]}} {{데이터베이스_아이디}}`
