# csvformat

> csvkit에 포함된 CSV 파일을 사용자 정의 출력으로 변환.
> 더 많은 정보: <https://csvkit.readthedocs.io/en/latest/scripts/csvformat.html>.

- 탭으로 구분된 파일(TSV)로 변환:

`csvformat -T {{데이터.csv}}`

- 구분자를 사용자 지정 문자로 변환:

`csvformat -D "{{사용자_지정_문자}}" {{데이터.csv}}`

- 라인의 끝을 캐리지 리턴 (^M) + 라인 바꿈으로 변환:

`csvformat -M "{{\r\n}}" {{데이터.csv}}`

- 인용문 사용 최소화:

`csvformat -U 0 {{데이터.csv}}`

- 인용문 사용 최대화:

`csvformat -U 1 {{데이터.csv}}`
