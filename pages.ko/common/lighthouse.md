# lighthouse

> 웹 애플리케이션과 웹 페이지를 분석하여 최신 성능 메트릭과 개발자 모범 사례에 대한 통찰을 수집합니다.
> 더 많은 정보: <https://github.com/GoogleChrome/lighthouse>.

- 특정 웹사이트에 대한 HTML 보고서를 생성하고 현재 디렉토리에 파일로 저장:

`lighthouse {{https://example.com}}`

- JSON 보고서를 생성하고 출력:

`lighthouse --output {{json}} {{https://example.com}}`

- JSON 보고서를 생성하고 특정 파일에 저장:

`lighthouse --output {{json}} --output-path {{경로/대상/파일.json}} {{https://example.com}}`

- 브라우저를 무헤드 모드로 사용하고 `stdout`에 기록하지 않고 보고서 생성:

`lighthouse --quiet --chrome-flags="{{--headless}}" {{https://example.com}}`

- 모든 요청에 대해 지정된 JSON 파일의 HTTP 헤더 키/값 쌍을 사용하여 보고서 생성:

`lighthouse --extra-headers={{경로/대상/파일.json}} {{https://example.com}}`

- 특정 카테고리만을 위한 보고서 생성:

`lighthouse --only-categories={{performance,accessibility,best-practices,seo,pwa}} {{https://example.com}}`

- 장치 에뮬레이션과 모든 제한을 비활성화하여 보고서 생성:

`lighthouse --screenEmulation.disabled --throttling-method={{provided}} --no-emulatedUserAgent {{https://example.com}}`

- 도움말 표시:

`lighthouse --help`
