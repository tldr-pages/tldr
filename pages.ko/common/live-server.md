# live-server

> 실시간 리로드 기능을 갖춘 간단한 개발 HTTP 서버.
> 더 많은 정보: <https://github.com/tapio/live-server>.

- `index.html` 파일을 제공하고 변경 시 리로드:

`live-server`

- 파일을 제공할 포트 지정 (기본값은 8080):

`live-server --port={{8081}}`

- 특정 파일을 제공:

`live-server --open={{about.html}}`

- ROUTE에 대한 모든 요청을 URL로 프록시:

`live-server --proxy={{/}}:{{http://localhost:3000}}`
