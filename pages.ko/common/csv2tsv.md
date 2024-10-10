# csv2tsv

> CSV (쉼표로 구분) 텍스트를 TSV (탭으로 구분) 형식으로 변환함.
> 더 많은 정보: <https://github.com/eBay/tsv-utils/blob/master/README.md#csv2tsv>.

- CSV를 TSV로 변환:

`csv2tsv {{경로/대상/입력_csv1 경로/대상/입력_csv2 ...}} > {{경로/대상/출력_csv}}`

- 필드 구분 기호로 구분되어 있는 CSV를 TSV로 변환:

`csv2tsv -c'{{field_delimiter}}' {{경로/대상/입력_csv}}`

- 세미콜론으로 구분된 CSV를 TSV로 변환:

`csv2tsv -c';' {{경로/대상/입력_csv}}`
