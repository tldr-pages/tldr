# mysqlbinlog

> MySQL 바이너리 로그 파일을 처리하는 도구.
> 더 많은 정보: <https://dev.mysql.com/doc/refman/en/mysqlbinlog.html>.

- 특정 바이너리 로그 파일에서 이벤트 표시:

`mysqlbinlog {{경로/대상/바인로그}}`

- 특정 데이터베이스에 대한 바이너리 로그의 항목 표시:

`mysqlbinlog --database {{데이터베이스_이름}} {{경로/대상/바인로그}}`

- 특정 날짜 사이의 바이너리 로그에서 이벤트 표시:

`mysqlbinlog --start-datetime='{{2022-01-01 01:00:00}}' --stop-datetime='{{2022-02-01 01:00:00}}' {{경로/대상/바인로그}}`

- 특정 위치 사이의 바이너리 로그에서 이벤트 표시:

`mysqlbinlog --start-position={{100}} --stop-position={{200}} {{경로/대상/바인로그}}`

- 지정된 호스트의 MySQL 서버에서 바이너리 로그 표시:

`mysqlbinlog --host={{호스트_이름}} {{경로/대상/바인로그}}`
