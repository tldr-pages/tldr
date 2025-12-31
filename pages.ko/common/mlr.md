# mlr

> Miller는 CSV, TSV 및 표 형식 JSON과 같은 이름으로 색인된 데이터를 위한 `awk`, `sed`, `cut`, `join`, `sort`와 유사합니다.
> 더 많은 정보: <https://miller.readthedocs.io/en/latest/manpage/>.

- CSV 파일을 표 형식으로 보기 좋게 출력:

`mlr --icsv --opprint cat {{예제.csv}}`

- JSON 데이터를 받아 출력 형식을 보기 좋게 출력:

`echo '{"hello":"world"}' | mlr --ijson --opprint cat`

- 특정 필드를 알파벳 순서로 정렬:

`mlr --icsv --opprint sort -f {{필드}} {{예제.csv}}`

- 특정 필드를 내림차순 숫자 순서로 정렬:

`mlr --icsv --opprint sort -nr {{필드}} {{예제.csv}}`

- CSV를 JSON으로 변환하며 계산 수행 및 계산 결과 표시:

`mlr --icsv --ojson put '${{새필드1}} = ${{옛필드A}}/${{옛필드B}}' {{예제.csv}}`

- JSON을 받아 출력 형식을 수직 JSON으로 포맷:

`echo '{"hello":"world", "foo":"bar"}' | mlr --ijson --ojson --jvstack cat`

- 압축된 CSV 파일의 숫자를 문자열로 처리하여 행 필터링:

`mlr --prepipe 'gunzip' --csv filter -S '${{필드명}} =~ "{{정규_표현식}}"' {{예제.csv.gz}}`
