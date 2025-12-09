# doctl databases replica

> 데이터베이스 클러스터와 연결된 읽기 전용 복제본을 관리.
> 더 많은 정보: <https://docs.digitalocean.com/reference/doctl/reference/databases/replica/>.

- 액세스 토큰을 사용하여 `doctl databases replica` 명령을 실행:

`doctl databases pool {{명령어}} --access-token {{액세스_토큰}}`

- 읽기 전용 데이터베이스 복제본에 대한 정보를 검색:

`doctl databases replica get {{데이터베이스_아이디}} {{복제본_이름}}`

- 읽기 전용 데이터베이스 복제본 목록 검색:

`doctl databases replica list {{데이터베이스_아이디}}`

- 읽기 전용 데이터베이스 복제본 생성:

`doctl databases replica create {{데이터베이스_아이디}} {{복제본_이름}}`

- 읽기 전용 데이터베이스 복제본 삭제:

`doctl databases replica delete {{데이터베이스_아이디}} {{복제본_이름}}`
