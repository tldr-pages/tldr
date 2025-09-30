# mate-search-tool

> MATE 데스크톱 환경에서 파일 검색.
> 더 많은 정보: <https://manned.org/mate-search-tool>.

- 특정 디렉토리에서 이름에 특정 문자열이 포함된 파일 검색:

`mate-search-tool --named={{문자열}} --path={{경로/대상/폴더}}`

- 사용자 확인을 기다리지 않고 파일 검색:

`mate-search-tool --start --named={{문자열}} --path={{경로/대상/폴더}}`

- 특정 정규 표현식과 일치하는 이름의 파일 검색:

`mate-search-tool --start --regex={{문자열}} --path={{경로/대상/폴더}}`

- 검색 결과 정렬 순서 설정:

`mate-search-tool --start --named={{문자열}} --path={{경로/대상/폴더}} --sortby={{name|folder|size|type|date}}`

- 내림차순 정렬 설정:

`mate-search-tool --start --named={{문자열}} --path={{경로/대상/폴더}} --descending`

- 특정 사용자/그룹 소유의 파일 검색:

`mate-search-tool --start --{{user|group}}={{값}} --path={{경로/대상/폴더}}`
