# csvgrep

> csvkit에 포함된 CSV행의 문자열 및 패턴 매칭 필터링.
> 더 많은 정보: <https://csvkit.readthedocs.io/en/latest/scripts/csvgrep.html>.

- 1 열에 특정 문자열이 있는 행 찾기:

`csvgrep -c {{1}} -m {{찾을_문자열}} {{데이터.csv}}`

- 3열 또는 4열에서 특정 정규식 패턴과 일치하는 행 찾기:

`csvgrep -c {{3,4}} -r {{정규식_패턴}} {{데이터.csv}}`

- "이름" 열에서 "John Doe"가 포함되지 않는 행 찾기:

`csvgrep -i -c {{이름}} -m "{{John Doe}}" {{데이터.csv}}`
