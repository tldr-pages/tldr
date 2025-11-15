# csvcut

> 유닉스의 `cut` 명령어와 같이 CSV 파일 필터링 및 잘라내기, tabular 데이터 보존을 위해. csvkit에 포함된 CSV 파일만 해당.
> 더 많은 정보: <https://csvkit.readthedocs.io/en/latest/scripts/csvcut.html>.

- 모든 열의 인덱스 및 이름 출력:

`csvcut -n {{데이터.csv}}`

- 첫번째 및 세번째 열 출력:

`csvcut -c {{1,3}} {{데이터.csv}}`

- 네번째 열을 제외한 모든 열 출력:

`csvcut -C {{4}} {{데이터.csv}}`

- "id" 및 "first name" (이 순서대로) 열 출력:

`csvcut -c {{id,"first name"}} {{데이터.csv}}`
