# sqlite3

> SQLite 3의 명령줄 인터페이스로, 자체 포함 파일 기반 임베디드 SQL 엔진입니다.
> 더 많은 정보: <https://sqlite.org/cli.html>.

- 새 데이터베이스로 대화형 셸 시작:

`sqlite3`

- 기존 데이터베이스로 대화형 셸 열기:

`sqlite3 {{경로/대상/데이터베이스.sqlite3}}`

- 데이터베이스에 SQL 문 실행 후 종료:

`sqlite3 {{경로/대상/데이터베이스.sqlite3}} '{{SELECT * FROM some_table;}}'`
