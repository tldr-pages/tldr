# csvstat

> csvkit에 포함된 CSV 파일의 모든 열에 대한 설명 통계 출력.
> 더 많은 정보: <https://csvkit.readthedocs.io/en/latest/scripts/csvstat.html>.

- 모든 열에 대한 정보 출력:

`csvstat {{데이터.csv}}`

- 2열 , 4열의 모든 정보 출력:

`csvstat -c {{2,4}} {{데이터.csv}}`

- 모든 열의 합계 출력:

`csvstat --sum {{data.csv}}`

- 3열에 대한 최대값 길이 출력:

`csvstat -c {{3}} --len {{데이터.csv}}`

- "이름" 열에 고유 값의 수 출력:

`csvstat -c {{이름}} --unique {{데이터.csv}}`
