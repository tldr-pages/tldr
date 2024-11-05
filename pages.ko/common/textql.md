# textql

> CSV 또는 TSV 파일과 같은 구조화된 텍스트에 대해 SQL을 실행.
> 더 많은 정보: <https://github.com/dinedal/textql>.

- 특정 CSV 파일에서 SQL 쿼리와 일치하는 줄을 `stdout`에 출력:

`textql -sql "{{SELECT * FROM filename}}" {{경로/대상/파일명.csv}}`

- TSV 파일 쿼리:

`textql -dlm=tab -sql "{{SELECT * FROM filename}}" {{경로/대상/파일명.tsv}}`

- 헤더 행이 있는 파일 쿼리:

`textql -dlm={{구분자}} -header -sql "{{SELECT * FROM filename}}" {{경로/대상/파일명.csv}}`

- `stdin`에서 데이터 읽기:

`cat {{경로/대상/파일}} | textql -sql "{{SELECT * FROM stdin}}"`

- 지정된 공통 열로 두 파일 조인:

`textql -header -sql "SELECT * FROM {{경로/대상/파일1}} JOIN {{파일2}} ON {{경로/대상/파일1}}.{{c1}} = {{파일2}}.{{c1}} LIMIT {{10}}" -output-header {{경로/대상/파일1.csv}} {{경로/대상/파일2.csv}}`

- 출력 구분자와 출력 헤더 라인을 사용하여 출력 형식 지정:

`textql -output-dlm={{구분자}} -output-header -sql "SELECT {{열}} AS {{별칭}} FROM {{파일명}}" {{경로/대상/파일명.csv}}`
