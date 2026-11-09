# wcurl

> 파일을 쉽게 다운로드할 수 있는 간단한 `curl` 래퍼.
> 관련 항목: `wget`, `curl`.
> 더 많은 정보: <https://curl.se/wcurl/manual.html>.

- URL의 내용을 URL이 나타내는 파일(이 경우 `index.html`)로 다운로드:

`wcurl {{https://example.com/index.html}}`

- URL의 내용을 지정된 이름의 파일로 다운로드:

`wcurl {{[-o|--output]}} {{경로/대상/파일}} {{https://example.com/index.html}}`

- 진행률 표시줄을 활성화하고 HTTP/2를 기본으로 사용하여 URL 내용 다운로드:

`wcurl --curl-options "--progress-bar --http2" {{https://example.com/index.html}}`

- 중단된 다운로드 이어받기:

`wcurl --curl-options "--clobber --continue-at -" {{https://example.com/index.html}}`
