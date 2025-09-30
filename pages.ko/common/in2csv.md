# in2csv

> 다양한 표 데이터 형식을 CSV로 변환.
> csvkit에 포함.
> 더 많은 정보: <https://csvkit.readthedocs.io/en/latest/scripts/in2csv.html>.

- XLS 파일을 CSV로 변환:

`in2csv {{data.xls}}`

- DBF 파일을 CSV 파일로 변환:

`in2csv {{data.dbf}} > {{data.csv}}`

- 특정 시트를 XLSX 파일에서 CSV로 변환:

`in2csv --sheet={{시트_이름}} {{data.xlsx}}`

- JSON 파일을 in2csv로 파이프:

`cat {{data.json}} | in2csv -f json > {{data.csv}}`
