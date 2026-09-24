# hugo server

> Hugo의 내장 웹서버를 사용하여 사이트를 빌드하고 실행.
> 더 많은 정보: <https://gohugo.io/commands/hugo_server/>.

- 사이트를 빌드하고 실행:

`hugo server`

- 지정한 포트 번호로 사이트를 빌드하고 실행:

`hugo server {{[-p|--port]}} {{포트_번호}}`

- 지원되는 출력 형식(HTML, XML 등)을 최소화하여 사이트 실행:

`hugo server --minify`

- 프로덕션 환경에서 사이트를 빌드하고 실행하며, 전체 리렌더링을 수행하고, 지원되는 출력 형식을 최소화:

`hugo server {{[-e|--environment]}} {{production}} --disableFastRender --minify`

- 도움말 표시:

`hugo server {{[-h|--help]}}`
