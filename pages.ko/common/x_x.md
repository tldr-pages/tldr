# x_x

> Excel 및 CSV 파일 보기.
> 더 많은 정보: <https://github.com/kristianperkins/x_x>.

- XLSX 또는 CSV 파일 보기:

`x_x {{파일.xlsx|파일.csv}}`

- 첫 번째 행을 테이블 헤더로 사용하여 XLSX 또는 CSV 파일 보기:

`x_x -h {{0}} {{파일.xlsx|파일.csv}}`

- 비전형적인 구분 기호를 사용하는 CSV 파일 보기:

`x_x --delimiter={{';'}} --quotechar={{'|'}} {{파일.csv}}`
