# mysqld

> MySQL 데이터베이스 서버 시작.
> 더 많은 정보: <https://dev.mysql.com/doc/refman/en/mysqld.html>.

- MySQL 데이터베이스 서버 시작:

`mysqld`

- 서버 시작 및 오류 메시지를 콘솔에 출력:

`mysqld --console`

- 서버 시작 및 로그 출력을 사용자 지정 로그 파일에 저장:

`mysqld --log={{경로/대상/파일.log}}`

- 기본 인자와 그 값을 출력하고 종료:

`mysqld --print-defaults`

- 파일에서 인자와 값을 읽어 서버 시작:

`mysqld --defaults-file={{경로/대상/파일}}`

- 사용자 지정 포트에서 서버 시작:

`mysqld --port={{포트}}`

- 도움말 표시:

`mysqld --verbose --help`
