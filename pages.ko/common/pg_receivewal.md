# pg_receivewal

> PostgreSQL 클러스터의 write-ahead log을 스트리밍함.
> 더 많은 정보: <https://www.postgresql.org/docs/current/app-pgreceivewal.html>.

- WAL을 로컬 디렉토리로 스트리밍 (최소 필수 옵션):

`pg_receivewal {{[-D|--directory]}} {{디렉토리}}`

- 호스트, 포트, 사용자명을 지정하고 자세한 출력과 함께 WAL 스트리밍:

`pg_receivewal {{[-v|--verbose]}} {{[-h|--host]}} {{호스트}} {{[-p|--port]}} {{포트}} {{[-U|--username]}} {{사용자명}} {{[-D|--directory]}} {{디렉토리}}`

- 복제 슬롯(replication slot) 사용 (필요 시 생성):

`pg_receivewal {{[-S|--slot]}} {{slot_name}} --create-slot {{[-h|--host]}} {{호스트}} {{[-p|--port]}} {{포트}} {{[-U|--username]}} {{사용자명}} {{[-D|--directory]}} {{디렉토리}}`

- 지정한 WAL 위치 (LSN)까지 스트리밍:

`pg_receivewal {{[-E|--endpos]}} {{lsn}} {{[-D|--directory]}} {{디렉토리}} {{[-h|--host]}} {{호스트}} {{[-p|--port]}} {{포트}} {{[-U|--username]}} {{사용자명}}`

- 오류 발생 시 재시도(루프) 비활성화:

`pg_receivewal {{[-n|--no-loop]}} {{[-D|--directory]}} {{디렉토리}} {{[-h|--host]}} {{호스트}} {{[-p|--port]}} {{포트}} {{[-U|--username]}} {{사용자명}}`

- 동기식 flush 수행 (WAL 데이터를 즉시 디스크에 기록):

`pg_receivewal --synchronous {{[-D|--directory]}} {{디렉토리}} {{[-h|--host]}} {{호스트}} {{[-p|--port]}} {{포트}} {{[-U|--username]}} {{사용자명}}`

- WAL 출력을 압축하여 저장 (`gzip`, 압출 레벨 0-9):

`pg_receivewal {{[-Z|--compress]}} {{level|method}} {{[-D|--directory]}} {{디렉토리}} {{[-h|--host]}} {{호스트}} {{[-p|--port]}} {{포트}} {{[-U|--username]}} {{사용자명}}`

- 상태 보고 간격 설정:

`pg_receivewal {{[-s|--status-interval]}} {{초}} {{[-D|--directory]}} {{디렉토리}} {{[-h|--host]}} {{호스트}} {{[-p|--port]}} {{포트}} {{[-U|--username]}} {{사용자명}}`
