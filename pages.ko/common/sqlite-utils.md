# sqlite-utils

> SQLite 데이터베이스를 다양한 방식으로 조작하기 위한 명령줄 도구.
> 더 많은 정보: <https://sqlite-utils.datasette.io/en/stable/cli.html>.

- 데이터베이스 생성:

`sqlite-utils create-database {{경로/대상/database.db}}`

- 테이블 생성:

`sqlite-utils create-table {{경로/대상/database.db}} {{테이블_이름}} {{id integer name text height float photo blob --pk id}}`

- 테이블 목록:

`sqlite-utils tables {{경로/대상/database.db}}`

- 레코드 삽입 또는 업데이트:

`{{echo '[ {"id": 1, "name": "Linus Torvalds"}, {"id": 2, "name": "Steve Wozniak"}, {"id": 3, "name": "Tony Hoare"} ]'}} | sqlite-utils upsert {{경로/대상/database.db}} {{테이블_이름}} - {{--pk id}}`

- 레코드 선택:

`sqlite-utils rows {{경로/대상/database.db}} {{테이블_이름}}`

- 레코드 삭제:

`sqlite-utils query {{경로/대상/database.db}} "{{delete from table_name where name = 'Tony Hoare'}}"`

- 테이블 삭제:

`sqlite-utils drop-table {{경로/대상/database.db}} {{테이블_이름}}`

- 도움말 표시:

`sqlite-utils -h`
