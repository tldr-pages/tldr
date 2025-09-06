# serve

> 정적 파일 제공 및 디렉토리 목록화 도구.
> 더 많은 정보: <https://github.com/vercel/serve>.

- 기본 포트에서 현재 디렉토리를 제공하는 HTTP 서버 시작:

`serve`

- 특정 [p]포트에서 특정 디렉토리를 제공하는 HTTP 서버 시작:

`serve -p {{포트}} {{경로/대상/폴더}}`

- 모든 응답에 `Access-Control-Allow-Origin: *` 헤더를 포함하여 CORS가 활성화된 HTTP 서버 시작:

`serve --cors`

- 모든 찾을 수 없는 요청을 `index.html` 파일로 리다이렉트하는 기본 포트의 HTTP 서버 시작:

`serve --single`

- 지정된 인증서를 사용하여 기본 포트에서 HTTPS 서버 시작:

`serve --ssl-cert {{경로/대상/인증서.pem}} --ssl-key {{경로/대상/키.pem}}`

- 특정 구성 파일을 사용하여 기본 포트에서 HTTP 서버 시작:

`serve --config {{경로/대상/서버.json}}`

- 도움말 표시:

`serve --help`
