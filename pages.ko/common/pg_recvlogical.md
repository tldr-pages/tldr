# pg_recvlogical

> PostgreSQL 논리 디코딩 스트림을 제어.
> 더 많은 정보: <https://www.postgresql.org/docs/current/app-pgrecvlogical.html>.

- 새로운 논리 복제 슬롯 생성:

`pg_recvlogical {{[-d|--dbname]}} {{데이터베이스_이름}} {{[-S|--slot]}} {{슬롯_이름}} --create-slot`

- 논리 복제 슬롯의 변경 사항을 파일로 스트리밍:

`pg_recvlogical {{[-d|--dbname]}} {{데이터베이스_이름}} {{[-S|--slot]}} {{슬롯_이름}} --start {{[-f|--file]}} {{파일이름}}`

- 논리 복제 슬롯 삭제:

`pg_recvlogical {{[-d|--dbname]}} {{데이터베이스_이름}} {{[-S|--slot]}} {{슬롯_이름}} --drop-slot`

- two-phase commit이 활성화된 논리 복제 슬롯 생성:

`pg_recvlogical {{[-d|--dbname]}} {{데이터베이스_이름}} {{[-S|--slot]}} {{슬롯_이름}} --create-slot {{[-t|--enable-two-phase]}}`

- 도움말 표시:

`pg_recvlogical {{[-?|--help]}}`
