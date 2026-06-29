# mariadb

> Mariadb 클라이언트 도구.
> 더 많은 정보: <https://mariadb.com/docs/server/clients-and-utilities/mariadb-client/mariadb-command-line-client>.

- 현재 사용자로 MariaDB 접속:

`mariadb`

- 특정 MariaDB 데이터베이스에 연결:

`mariadb {{데이터베이스_이름}}`

- 사용자명과 비밀번호를 사용하여 MariaDB 데이터베이스에 접속:

`mariadb {{[-u|--user]}} {{사용자_이름}} {{[-p|--password]}} {{자신의_비밀번호}} {{데이터베이스_이름}}`

- 대화형 모드 및 배치 모드에서 각 SQL 문 실행 후에 경고를 표시:

`mariadb --show-warning`

- 출력 메시지를 간소화하여 표시 (-s를 여러 번 사용할수록 더 적은 정보 출력):

`mariadb {{-s|-ss|-sss|--silent}}`

- SQL 스크립트 파일 실행 후 결과를 파일로 저장:

`mariadb < {{경로/대상/스크립트.sql}} {{데이터베이스_이름}} > {{경로/대상/출력파일.tab}}`

- 종료 시 메모리 사용량 및 열린 파일 정보 점검:

`mariadb --debug-check`

- 로컬 연결을 위해 소켓 파일을 사용하여 접속:

`mariadb {{[-S|--socket]}} {{경로/대상/소켓_이름}}`
