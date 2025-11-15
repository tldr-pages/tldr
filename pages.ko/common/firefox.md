# firefox

> 무료 오픈 소스 웹 브라우저.
> 더 많은 정보: <https://wiki.mozilla.org/Firefox/CommandLineOptions>.

- Firefox를 실행하고 웹 페이지 열기:

`firefox {{https://www.duckduckgo.com}}`

- 새로운 창 열기:

`firefox --new-window {{https://www.duckduckgo.com}}`

- 비공개 (시크릿) 창을 열기:

`firefox --private-window`

- 기본 검색 엔진을 사용하여 "wikipedia"를 검색:

`firefox --search "{{wikipedia}}"`

- 모든 확장 기능을 비활성화한 상태에서 안전 모드로 Firefox를 실행:

`firefox --safe-mode`

- 헤드리스 모드에서 웹 페이지의 스크린샷을 찍음:

`firefox --headless --screenshot {{경로/대상/출력_파일.png}} {{https://example.com/}}`

- 특정 프로필을 사용하여 여러 개의 개별 Firefox 인스턴스를 동시에 실행:

`firefox --profile {{경로/대상/디렉토리}} {{https://example.com/}}`

- Firefox를 기본 브라우저로 설정:

`firefox --setDefaultBrowser`
