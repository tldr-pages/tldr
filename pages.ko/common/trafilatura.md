# trafilatura

> 웹 페이지에서 본문, 메타데이터 및 댓글을 추출하는 Python 기반 웹 스크래핑, 크롤링 도구.
> 텍스트 코퍼스 생성과 구조화된 콘텐츠 추출에 적합.
> 더 많은 정보: <https://trafilatura.readthedocs.io/en/latest/usage-cli.html#further-information>.

- URL에서 텍스트 추출:

`trafilatura {{[-u|--URL]}} {{주소}}`

- 텍스트를 추출하여 파일에 저장:

`trafilatura {{[-u|--URL]}} {{주소}} {{[-o|--output-dir]}} {{경로/대상/출력파일.txt}}`

- 텍스트를 JSON 형식으로 추출:

`trafilatura {{[-u|--URL]}} {{주소}} --json`

- 파일에 나열된 여러 URL에서 텍스트 추출:

`trafilatura {{[-i|--input-file]}} {{경로/대상/url_목록.txt}}`

- 사이트맵을 사용해 웹사이트 크롤링:

`trafilatura --sitemap {{url_to_sitemap.xml}}`

- HTML 서식을 유지하며 텍스트 추출:

`trafilatura {{[-u|--URL]}} {{주소}} --formatting`

- 댓글을 포함해 텍스트 추출:

`trafilatura {{[-u|--URL]}} {{주소}} --with-comments`

- 도움말 표시:

`trafilatura {{[-h|--help]}}`
