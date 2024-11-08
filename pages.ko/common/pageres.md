# pageres

> 다양한 해상도로 웹사이트의 스크린샷을 캡처.
> 더 많은 정보: <https://github.com/sindresorhus/pageres-cli>.

- 여러 URL의 다양한 해상도로 스크린샷 촬영:

`pageres {{https://example.com/}} {{https://example2.com/}} {{1366x768}} {{1600x900}}`

- 특정 URL에 대해 글로벌 옵션을 무시하고 특정 옵션 제공:

`pageres [{{https://example.com/}} {{1366x768}} --no-crop] [{{https://example2.com/}} {{1024x768}}] --crop`

- 사용자 정의 파일명 템플릿 제공:

`pageres {{https://example.com/}} {{1024x768}} --filename={{'<%= date %> - <%= url %>'}}`

- 페이지의 특정 요소 캡처:

`pageres {{https://example.com/}} {{1366x768}} --selector='{{.page-header}}'`

- 특정 요소 숨기기:

`pageres {{https://example.com/}} {{1366x768}} --hide='{{.page-header}}'`

- 로컬 파일의 스크린샷 캡처:

`pageres {{local_file_path.html}} {{1366x768}}`
