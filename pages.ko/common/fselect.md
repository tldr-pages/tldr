# fselect

> SQL과 유사한 쿼리로 파일을 찾음.
> 더 많은 정보: <https://github.com/jhspetersson/fselect>.

- 특정 디렉터리의 임시 또는 구성 파일에서 전체 경로와 크기를 선택:

`fselect size, path from {{경로/대상/디렉토리}} where name = {{'*.cfg'}} or name = {{'*.tmp'}}`

- 정사각형 이미지 찾기:

`fselect path from {{경로/대상/디렉토리}} where width = height`

- 옛날 랩 320kbps MP3 파일 찾기:

`fselect path from {{경로/대상/디렉토리}} where genre = {{Rap}} and bitrate = {{320}} and mp3_year lt {{2000}}`

- 처음 5개 결과만 선택하고 JSON으로 출력:

`fselect size, path from {{경로/대상/디렉토리}} limit {{5}} into json`

- SQL 집계 함수를 사용하여, 디렉터리에 있는 파일의 최소, 최대 및 평균 크기를 계산:

`fselect "{{MIN(size), MAX(size), AVG(size), SUM(size), COUNT(*)}} from {{경로/대상/디렉토리}}"`
