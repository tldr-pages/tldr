# query

> 프로세스, 세션 및 원격 데스크톱 세션 호스트 서버에 대한 정보를 표시합니다.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/query>.

- 모든 사용자 세션 표시:

`query session`

- 원격 컴퓨터의 현재 사용자 세션 표시:

`query session /server:{{호스트명}}`

- 로그인한 사용자 표시:

`query user`

- 원격 컴퓨터의 모든 사용자 세션 표시:

`query session /server:{{호스트명}}`

- 모든 실행 중인 프로세스 표시:

`query process`

- 세션 또는 사용자 이름별 실행 중인 프로세스 표시:

`query process {{세션명|사용자명}}`
