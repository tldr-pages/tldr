# tabula

> PDF 파일에서 테이블을 추출.
> 더 많은 정보: <https://github.com/tabulapdf/tabula-java#commandline-usage-examples>.

- PDF에서 모든 테이블을 CSV 파일로 추출:

`tabula -o {{파일.csv}} {{파일.pdf}}`

- PDF에서 모든 테이블을 JSON 파일로 추출:

`tabula --format JSON -o {{파일.json}} {{파일.pdf}}`

- PDF의 1, 2, 3, 6 페이지에서 테이블 추출:

`tabula --pages {{1-3,6}} {{파일.pdf}}`

- PDF의 1 페이지에서 테이블을 추출하며, 분석할 페이지의 부분을 추측:

`tabula --guess --pages {{1}} {{파일.pdf}}`

- 셀 경계를 결정하기 위해 줄을 사용하여 PDF에서 모든 테이블 추출:

`tabula --spreadsheet {{파일.pdf}}`

- 셀 경계를 결정하기 위해 빈 공간을 사용하여 PDF에서 모든 테이블 추출:

`tabula --no-spreadsheet {{파일.pdf}}`
