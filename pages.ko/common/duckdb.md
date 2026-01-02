# duckdb

> 처리 중인 분석 SQL 엔진인 DuckDB용 명령줄 클라이언트.
> 더 많은 정보: <https://duckdb.org/docs/stable/clients/cli/arguments>.

- 임시 메모리 내 데이터베이스를 사용하여 대화형 쉘을 시작:

`duckdb`

- 데이터베이스 파일에서 대화형 쉘을 시작. 파일이 없으면, 새로운 데이터베이스가 생성됨:

`duckdb {{경로/대상/데이터베이스파일}}`

- CSV, JSON 또는 Parquet 파일을 직접 쿼리:

`duckdb -c "{{SELECT * FROM 'data_source.[csv|csv.gz|json|json.gz|parquet]'}}"`

- SQL 스크립트를 실행:

`duckdb -c ".read {{경로/대상/스크립트.sql}}"`

- 데이터베이스 파일에 대해 쿼리를 실행하고 대화형 쉘을 열어둠:

`duckdb {{경로/대상/데이터베이스파일}} -cmd "{{SELECT DISTINCT * FROM tbl}}"`

- 데이터베이스 파일에서 SQL 쿼리를 실행하고 대화형 쉘을 열어둠:

`duckdb {{경로/대상/데이터베이스파일}} -init {{경로/대상/스크립트.sql}}`

- `stdin`에서 CSV를 읽고 `stdout`에 CSV를 쓰기:

`cat {{경로/대상/소스.csv}} | duckdb -c "{{COPY (FROM read_csv('/dev/stdin')) TO '/dev/stdout' WITH (FORMAT CSV, HEADER)}}"`

- 도움말 표시:

`duckdb -help`
