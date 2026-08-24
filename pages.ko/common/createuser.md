# createuser

> PostgreSQL 사용자(역할)를 생성.
> 더 많은 정보: <https://www.postgresql.org/docs/current/app-createuser.html>.

- 대화형으로 사용자를 생성:

`createuser --interactive {{사용자명}}`

- 특별한 권한 없이 사용자를 생성:

`createuser {{사용자명}}`

- 슈퍼유저를 생성:

`createuser {{[-s|--superuser]}} {{사용자명}}`

- 데이터베이스 생성 권한, 역할 관리, 비밀번호 입력을 요청하는 사용자를 생성:

`createuser {{[-d|--createdb]}} {{[-r|--createrole]}} {{[-P|--pwprompt]}} {{사용자명}}`

- 데이터베이스 생성 및 역할 관리 권한이 없는 사용자를 생성:

`createuser {{[-D|--no-createdb]}} {{[-R|--no-createrole]}} {{사용자명}}`
