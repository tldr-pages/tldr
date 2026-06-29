# pg_createsubscriber

> 물리적 복제본을 새로운 논리적 복제본으로 변환.
> 더 많은 정보: <https://www.postgresql.org/docs/current/app-pgcreatesubscriber.html>.

- 특정 데이터베이스의 물리적 복제본을 논리적 복제본으로 변환:

`pg_createsubscriber {{[-d|--database]}} {{데이터베이스_이름}} {{[-D|--pgdata]}} {{경로/대상/데이터}} {{[-P|--publisher-server]}} {{connstr}}`

- dry run 수행 (대상 디렉터리를 변경하지 않음):

`pg_createsubscriber {{[-n|--dry-run]}} {{[-d|--database]}} {{데이터베이스_이름}} {{[-D|--pgdata]}} {{경로/대상/데이터}} {{[-P|--publisher-server]}} {{connstr}}`

- 구독에 Two-phase commit 활성화:

`pg_createsubscriber {{[-T|--enable-two-phase]}} {{[-d|--database]}} {{데이터베이스_이름}} {{[-D|--pgdata]}} {{경로/대상/데이터}} {{[-P|--publisher-server]}} {{connstr}}`

- 자세한 출력과 함께 변환:

`pg_createsubscriber {{[-v|--verbose]}} {{[-d|--database]}} {{데이터베이스_이름}} {{[-D|--pgdata]}} {{경로/대상/데이터}} {{[-P|--publisher-server]}} {{connstr}}`

- 도움말 표시:

`pg_createsubscriber {{[-?|--help]}}`
