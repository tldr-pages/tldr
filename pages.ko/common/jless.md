# jless

> JSON 데이터를 대화형으로 탐색하고 확인.
> 관련 항목: `jq`, `fx`, `less`.
> 더 많은 정보: <https://jless.io/user-guide>.

- JSON 파일 열기:

`jless {{경로/대상/파일.json}}`

- `stdin`에서 JSON 데이터 읽기:

`cat {{경로/대상/파일.json}} | jless`

- 파일 확장자와 관계없이 YAML 형식으로 파싱:

`jless --yaml {{경로/대상/파일}}`

- 라인 모드로 시작 (중괄호, 쉼표 및 따옴표로 감싼 객체 키 표시):

`jless {{[-m|--mode]}} line {{경로/대상/파일.json}}`

- 줄 번호 숨기기:

`jless {{[-N|--no-line-numbers]}} {{경로/대상/파일.json}}`

- 상대 줄 번호 표시:

`jless {{[-r|--relative-line-numbers]}} {{경로/대상/파일.json}}`

- [대화형] 패턴을 앞으로 검색 (`<n>`/`<N>`으로 다음/이전 일치 항목 이동):

`</>{{pattern}}`

- [대화형] 종료:

`<q>`
