# mysides

> Finder 즐겨찾기 추가, 나열 및 제거 도구.
> 더 많은 정보: <https://github.com/mosen/mysides>.

- 사이드바 즐겨찾기 나열:

`mysides list`

- 새로운 항목을 사이드바 즐겨찾기 끝에 추가:

`mysides add {{예시}} {{file:///Users/Shared/example}}`

- 이름으로 항목 제거:

`mysides remove {{예시}}`

- 현재 디렉토리를 사이드바에 추가:

`mysides add $(basename $(pwd)) file:///$(pwd)`

- 현재 디렉토리를 사이드바에서 제거:

`mysides remove $(basename $(pwd))`
