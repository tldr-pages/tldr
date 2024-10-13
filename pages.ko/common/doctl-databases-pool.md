# doctl databases pool

> 데이터베이스 클러스터의 연결 풀을 관리.
> 더 많은 정보: <https://docs.digitalocean.com/reference/doctl/reference/databases/pool/>.

- 액세스 토큰을 사용하여 `doctl databases pool` 명령을 실행:

`doctl databases pool {{명령어}} --access-token {{액세스_토큰}}`

- 데이터베이스 연결 풀에 대한 정보 검색:

`doctl databases pool get {{데이터베이스_아이디}} {{풀_이름}}`

- 데이터베이스 클러스터에 대한 연결 풀을 나열:

`doctl databases pool list {{데이터베이스_아이디}}`

- 데이터베이스에 대한 연결 풀을 생성:

`doctl databases pool create {{데이터베이스_아이디}} {{풀_이름}} --db {{새로운_풀_이름}} --size {{풀_크기}}`

- 데이터베이스에 대한 연결 풀을 삭제:

`doctl databases pool create {{데이터베이스_아이디}} {{풀_이름}}`
