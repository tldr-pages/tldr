# you-get

> 웹에서 미디어 콘텐츠(비디오, 오디오, 이미지)를 다운로드.
> 같이 보기: `yt-dlp`, `youtube-viewer`, `instaloader`.
> 더 많은 정보: <https://you-get.org/#getting-started>.

- 웹의 특정 미디어에 대한 정보 출력:

`you-get --info {{https://example.com/video?id=value}}`

- 특정 URL에서 미디어 다운로드:

`you-get {{https://example.com/video?id=value}}`

- Google Videos에서 검색 및 다운로드:

`you-get {{키워드}}`

- 특정 위치에 미디어 다운로드:

`you-get --output-dir {{경로/대상/폴더}} --output-filename {{파일명}} {{https://example.com/watch?v=value}}`

- 프록시를 사용하여 미디어 다운로드:

`you-get --http-proxy {{프록시_서버}} {{https://example.com/watch?v=value}}`
