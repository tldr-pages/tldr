# dropuser

> PostgreSQL 사용자(역할)을 삭제하는 도구.
> 더 많은 정보: <https://www.postgresql.org/docs/current/app-dropuser.html>.

- 사용자 삭제 전 확인 및 사용자 이름 입력 요청:

`dropuser {{[-i|--interactive]}}`

- 사용자 즉시 삭제:

`dropuser {{사용자명}}`

- 존재하지 않는 사용자일 경우 오류 없이 처리:

`dropuser --if-exists {{사용자명}}`

- 127.0.0.1:4321 서버에서 사용자 삭제:

`dropuser {{[-h|--host]}} 127.0.0.1 {{[-p|--port]}} 4321 {{사용자명}}`

- "admin" 사용자로 127.0.0.1:4321 서버에 접속하여 사용자 삭제:

`dropuser {{[-U|--username]}} admin {{[-h|--host]}} 127.0.0.1 {{[-p|--port]}} 4321 {{사용자명}}`
