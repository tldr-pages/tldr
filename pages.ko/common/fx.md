# fx

> JSON 데이터를 조회하고 처리하는 도구.
> 더 많은 정보: <https://fx.wtf/getting-started>.

- JSON 파일을 대화형으로 보기:

`fx {{경로/대상/파일.json}}`

- `stdin`으로 받은 JSON을 보기 좋게 출력하고 색상 적용:

`cat {{경로/대상/파일.json}} | fx`

- URL의 JSON 데이터 열기:

`curl {{url}} | fx`

- JavaScript 스타일 표현식으로 JSON 필터링:

`fx {{경로/대상/파일.json}} {{.name}}`

- TOML 입력 파일을 JSON으로 변환:

`fx --toml {{경로/대상/파일.toml}}`

- YAML 입력 파일을 JSON으로 변환:

`fx --yaml {{경로/대상/파일.yaml}}`
