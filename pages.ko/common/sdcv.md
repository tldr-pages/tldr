# sdcv

> StarDict, 명령줄 사전 클라이언트.
> 사전은 클라이언트와 별도로 제공됩니다.
> 더 많은 정보: <https://manned.org/sdcv>.

- `sdcv`를 대화형 모드로 시작:

`sdcv`

- 설치된 사전 나열:

`sdcv --list-dicts`

- 특정 사전에서 정의 표시:

`sdcv --use-dict {{사전_이름}} {{검색어}}`

- 퍼지 검색으로 정의 조회:

`sdcv {{검색어}}`

- 정확한 검색으로 정의 조회:

`sdcv --exact-search {{검색어}}`

- 정의를 JSON 형식으로 조회:

`sdcv --json {{검색어}}`

- 특정 디렉토리에서 사전 검색:

`sdcv --data-dir {{경로/대상/폴더}} {{검색어}}`
