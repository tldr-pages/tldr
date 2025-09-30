# dirb

> HTTP 기반 웹 서버의 디렉토리와 파일을 스캔합니다.
> 더 많은 정보: <https://manned.org/dirb>.

- 기본 단어 목록을 사용하여 웹 서버 스캔:

`dirb {{https://example.org}}`

- 사용자 정의 단어 목록을 사용하여 웹 서버 스캔:

`dirb {{https://example.org}} {{경로/대상/단어목록.txt}}`

- 비재귀적으로 웹 서버 스캔:

`dirb {{https://example.org}} -r`

- 지정된 사용자 에이전트와 쿠키를 사용하여 웹 서버 스캔:

`dirb {{https://example.org}} -a {{사용자_에이전트_스트링}} -c {{쿠키_스트링}}`
