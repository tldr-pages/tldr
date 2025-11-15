# doctl databases user

> 데이터베이스 사용자에 대한 세부 정보를 보고 생성.
> 더 많은 정보: <https://docs.digitalocean.com/reference/doctl/reference/databases/user>.

- 액세스 토큰을 사용하여 `doctl databases user` 명령을 실행:

`doctl databases user {{명령어}} --access-token {{access_token}}`

- 데이터베이스 사용자에 대한 세부 정보를 검색:

`doctl databases user get {{데이터베이스_아이디}} {{사용자_이름}}`

- 특정 데이터베이스에 대한 데이터베이스 사용자 목록을 검색:

`doctl databases user list {{데이터베이스_아이디}}`

- 특정 사용자의 인증 비밀번호를 재설정:

`doctl databases user reset {{데이터베이스_아이디}} {{사용자_이름}}`

- 특정 사용자에 대한 MySQL 인증 플러그인 재설정:

`doctl databases user reset {{데이터베이스_아이디}} {{사용자_이름}} {{caching_sha2_password|mysql_native_password}}`

- 주어진 사용자 이름으로 주어진 데이터베이스에 사용자를 생성:

`doctl databases user create {{데이터베이스_아이디}} {{사용자_이름}}`

- 주어진 사용자 이름을 가진 주어진 데이터베이스에서 사용자를 삭제:

`doctl databases user delete {{데이터베이스_아이디}} {{사용자_이름}}`
