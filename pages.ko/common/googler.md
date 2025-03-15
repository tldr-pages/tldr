# googler

> 명령줄에서 Google 검색하기.
> 더 많은 정보: <https://github.com/jarun/googler>.

- Google에서 키워드 검색:

`googler {{키워드}}`

- Google을 검색하고 웹 브라우저에서 첫 번째 결과를 열기:

`googler -j {{키워드}}`

- N개의 검색 결과 표시 (기본값 10):

`googler -n {{N}} {{키워드}}`

- 자동 맞춤법 교정 비활성화:

`googler -x {{키워드}}`

- 하나의 사이트에서 키워드를 검색:

`googler -w {{사이트}} {{키워드}}`

- Google 검색 결과를 JSON 형식으로 표시:

`googler --json {{키워드}}`

- 내부적으로 자체 업그레이드 수행:

`googler -u`

- 대화형 모드에서 도움말 표시:

`<?>`
