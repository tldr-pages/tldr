# zeroclaw gateway

> ZeroClaw용 게이트웨이 서버를 시작 (웹훅 및 API).
> 더 많은 정보: <https://github.com/zeroclaw-labs/zeroclaw#quick-start>.

- 기본 포트에서 게이트웨이 시작 (8080):

`zeroclaw gateway`

- 지정한 포트에서 게이트웨이 시작:

`zeroclaw gateway {{[-p|--port]}} {{8080}}`

- 사용 가능한 임의의 포트에서 게이트웨이 시작:

`zeroclaw gateway {{[-p|--port]}} 0`

- 지정한 호스트에서 게이트웨의 시작:

`zeroclaw gateway --host {{0.0.0.0}} {{[-p|--port]}} {{8080}}`

- 도움말 표시:

`zeroclaw gateway {{[-h|--help]}}`
