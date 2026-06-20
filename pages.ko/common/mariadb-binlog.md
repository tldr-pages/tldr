# mariadb-binlog

> MariaDB 바이너리 로그 파일을 처리하는 도구.
> 더 많은 정보: <https://manned.org/mariadb-binlog>.

- 특정 바이너리 로그 파일의 이벤트 조회:

`mariadb-binlog {{경로/대상/바이너리_로그}}`

- 특정 데이터베이스 관련 이벤트만 조회:

`mariadb-binlog {{[-d|--database]}} {{데이터베이스_이름}} {{경로/대상/바이너리_로그}}`

- 특정 기간의 이벤트만 조회:

`mariadb-binlog --start-datetime '{{2022-01-01 01:00:00}}' --stop-datetime '{{2022-02-01 01:00:00}}' {{경로/대상/바이너리_로그}}`

- 특정 바이너리 로그 위치 범위만 조회:

`mariadb-binlog {{[-j|--start-position]}} {{100}} --stop-position {{200}} {{경로/대상/바이너리_로그}}`

- 원격 MariaDB 서버의 바이너리 로그 조회:

`mariadb-binlog {{[-h|--host]}} {{호스트명}} {{경로/대상/바이너리_로그}}`
