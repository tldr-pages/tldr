# exo dbaas

> Exoscale DBaaS를 관리.
> 더 많은 정보: <https://community.exoscale.com/product/dbaas/>.

- 사용 가능한 데이터베이스 서비스 타입 목록 조회:

`exo dbaas type list`

- 특정 데이터베이스 서비스 타입의 플랜 목록을 조회:

`exo dbaas type show {{데이터베이스_서비스_타입}} --plans`

- 새로운 데이터베이스 서비스 생성 (서비스 접속을 위해 IP 필터 필수 지정):

`exo dbaas create {{데이터베이스_서비스_타입}} {{데이터베이스_서비스_타입_plan}} {{데이터베이스_서비스_이름}} --{{데이터베이스_서비스_타입}}-ip-filter {{1.2.3.4/32}}`

- 데이터베이스 서비스의 연결 URI 출력:

`exo dbaas show {{데이터베이스_서비스_이름}} --uri`

- 데이터베이스 서비스의 유지보수 요일 및 시간 설정:

`exo dbaas update {{데이터베이스_서비스_이름}} --maintenance-dow {{요일}} --maintenance-time {{HH:MM:SS}}`

- 특정 데이터베이스 서비스 유형에 대한 도움말 출력:

`exo dbaas {{subcommand}} --help-{{데이터베이스_서비스_타입}}`
