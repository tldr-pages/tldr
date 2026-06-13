# doctl databases firewalls

> 데이터베이스 클러스터의 방화벽을 관리.
> 더 많은 정보: <https://docs.digitalocean.com/reference/doctl/reference/databases/firewalls/>.

- 액세스 토큰을 사용하여 `doctl databases firewalls` 명령을 실행:

`doctl {{[d|databases]}} {{[fw|firewalls]}} {{명령어}} {{[-t|--access-token]}} {{액세스_토큰}}`

- 특정 데이터베이스에 대한 방화벽 규칙 목록을 검색:

`doctl {{[d|databases]}} {{[fw|firewalls]}} {{[ls|list]}}`

- 특정 데이터베이스에 데이터베이스 방화벽 규칙을 추가:

`doctl {{[d|databases]}} {{[fw|firewalls]}} {{[a|append]}} {{데이터베이스_아이디}} --rule {{droplet|k8s|ip_addr|tag|app}}:{{value}}`

- 특정 데이터베이스에 대한 방화벽 규칙을 추가:

`doctl {{[d|databases]}} {{[fw|firewalls]}} {{[rm|remove]}} {{데이터베이스_아이디}} {{룰_uuid}}`
