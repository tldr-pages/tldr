# trdsql

> CSV, LTSV, JSON, YAML, TBLN 파일에 SQL 쿼리를 실행.
> 더 많은 정보: <https://noborus.github.io/trdsql/>.

- 여러 JSON 파일의 객체 데이터를 헤더와 큰따옴표가 포함된 CSV 파일로 변환 (`-oh`):

`trdsql -ocsv -oh "SELECT * FROM {{경로/대상/directory/*.json}}" | sed 's/\([^,]*\)/"&"/g' > {{경로/대상/파일.csv}}`

- JSON 리스트를 테이블로 해석하고 내부 객체의 필드를 열로 사용 (`경로/대상/파일.json: {"list":[{"age":"26","name":"Tanaka"}]}`):

`trdsql "SELECT * FROM {{경로/대상/파일.json}}::.list"`

- 첫 번째 줄을 헤더로 사용하는 여러 CSV 파일의 데이터를 복잡한 SQL 쿼리로 처리 (`-ih`):

`trdsql -icsv -ih "SELECT {{경로/대상}} FROM {{경로/대상/파일*.csv}} WHERE column2 != '' ORDER BY {{열1}} GROUP BY {{열1}}"`

- 두 CSV 파일의 내용을 하나의 CSV 데이터로 병합:

`trdsql "SELECT {{열1,열2}} FROM {{경로/대상/file1.csv}} UNION SELECT {{경로/대상}} FROM {{경로/대상/file2.csv}}"`

- PostgreSQL 데이터베이스에 연결:

`trdsql -driver postgres -dsn "host={{호스트명}} port={{5433}} dbname={{데이터베이스_이름}}" "SELECT 1"`

- CSV 파일의 데이터를 사용하여 MySQL 데이터베이스에 테이블 생성:

`trdsql -driver mysql -dsn "{{사용자명}}:{{비밀번호}}@{{호스트명}}/{{데이터베이스}}" -ih "CREATE TABLE {{테이블}} ({{열1}} int, {{열2}} varchar(20)) AS SELECT {{열3}} AS {{열1}},{{열2}} FROM {{경로/대상/헤더_파일.csv}}"`

- 압축된 로그 파일의 데이터 표시:

`trdsql -iltsv "SELECT * FROM {{경로/대상/access.log.gz}}"`
