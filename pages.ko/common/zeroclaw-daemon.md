# zeroclaw daemon

> ZeroClaw의 전체 자율 런타임을 시작 (게이트웨이 + 채널 + 하트비트).
> 더 많은 정보: <https://github.com/zeroclaw-labs/zeroclaw#quick-start>.

- 기본 포트에서 데몬 시작 (8080):

`zeroclaw daemon`

- 지정한 포트에서 데몬 시작:

`zeroclaw daemon {{[-p|--port]}} {{8080}}`

- 사용 가능한 임의의 포트에서 데몬 시작:

`zeroclaw daemon {{[-p|--port]}} 0`

- 지정한 호스트에서 데몬 시작:

`zeroclaw daemon --host {{0.0.0.0}} {{[-p|--port]}} {{8080}}`

- 도움말 표시:

`zeroclaw daemon {{[-h|--help]}}`
