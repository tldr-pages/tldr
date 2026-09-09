# httrack

> 웹사이트를 다운로드하여 오프라인에서 탐색할 수 있도록 함.
> 더 많은 정보: <https://www.httrack.com/html/fcguide.html>.

- 웹사이트 미러링:

`httrack {{https://example.com}}`

- 웹사이트를 지정한 디렉터리에 미러링:

`httrack {{https://example.com}} {{[-O|--path]}} {{경로/대상/출력_디렉터리}}`

- 캐시를 사용해 중단된 미러링 작업 이어서 실행:

`httrack {{https://example.com}} {{[-O|--path]}} {{경로/대상/출력_디렉터리}} {{[-i|--continue]}}`

- 재귀 탐색 깊이 제한:

`httrack {{https://example.com}} {{[-r|--depth=]}}{{5}}`

- 첫 번째 단계 페이지의 모든 링크를 포함하여 미러링:

`httrack {{https://example.com}} {{[-Y|--mirrorlinks]}}`

- ZIP 파일을 제외하고 웹사이트 미러링:

`httrack {{https://example.com}} "-*.zip"`
