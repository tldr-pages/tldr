# surfraw

> 다양한 웹 검색 엔진을 검색.
> 각 웹사이트를 검색하는 방법을 알고 있는 elvi 모음으로 구성됨.
> 더 많은 정보: <https://manned.org/surfraw>.

- 지원되는 웹사이트 검색 스크립트(elvi) 목록 표시:

`surfraw -elvi`

- 특정 검색어로 elvi의 결과 페이지를 브라우저에서 열기:

`surfraw {{elvi}} "{{검색어}}"`

- elvi 설명 및 특정 옵션 표시:

`surfraw {{elvi}} -local-help`

- 특정 옵션을 사용하여 elvi로 검색하고 결과 페이지를 브라우저에서 열기:

`surfraw {{elvi}} {{elvi_옵션}} "{{검색어}}"`

- 특정 검색어에 대한 elvi의 결과 페이지 URL 표시:

`surfraw -print {{elvi}} "{{검색어}}"`

- 별칭을 사용하여 검색:

`sr {{elvi}} "{{검색어}}"`
