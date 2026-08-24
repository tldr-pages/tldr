# doctl databases maintenance-window

> 데이터베이스의 유지 관리 기간을 예약하고 일정을 확인.
> 더 많은 정보: <https://docs.digitalocean.com/reference/doctl/reference/databases/maintenance-window/>.

- 액세스 토큰을 사용하여 `doctl databases maintenance-window` 명령을 실행:

`doctl {{[d|databases]}} {{[mw|maintenance-window]}} {{command}} {{[-t|--access-token]}} {{액세스_토큰}}`

- 데이터베이스 클러스터의 유지 관리 기간에 대한 세부 정보를 검색:

`doctl {{[d|databases]}} {{[mw|maintenance-window]}} {{[g|get]}} {{데이터베이스_아이디}}`

- 데이터베이스 클러스터의 유지 관리 기간을 업데이트:

`doctl {{[d|databases]}} {{[mw|maintenance-window]}} {{[u|update]}} {{데이터베이스_아이디}} --day {{요일}} --hour {{24시간_형식의_시간}}`
