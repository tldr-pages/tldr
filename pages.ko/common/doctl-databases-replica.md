# doctl databases replica

> 데이터베이스 클러스터와 연결된 읽기 전용 복제본을 관리.
> 더 많은 정보: <https://docs.digitalocean.com/reference/doctl/reference/databases/replica/>.

- 액세스 토큰을 사용하여 `doctl databases replica` 명령을 실행:

`doctl {{[d|databases]}} {{[r|replica]}} {{명령어}} {{[-t|--access-token]}} {{액세스_토큰}}`

- 읽기 전용 데이터베이스 복제본에 대한 정보를 검색:

`doctl {{[d|databases]}} {{[r|replica]}} {{[g|get]}} {{데이터베이스_아이디}} {{복제본_이름}}`

- 읽기 전용 데이터베이스 복제본 목록 검색:

`doctl {{[d|databases]}} {{[r|replica]}} {{[ls|list]}} {{데이터베이스_아이디}}`

- 읽기 전용 데이터베이스 복제본 생성:

`doctl {{[d|databases]}} {{[r|replica]}} {{[c|create]}} {{데이터베이스_아이디}} {{복제본_이름}}`

- 읽기 전용 데이터베이스 복제본 삭제:

`doctl {{[d|databases]}} {{[r|replica]}} {{[rm|delete]}} {{데이터베이스_아이디}} {{복제본_이름}}`
