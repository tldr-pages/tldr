# ngrok

> 로컬에서 실행 중인 웹 서비스에 공용 엔드포인트로부터 안전한 터널을 생성하는 리버스 프록시.
> 더 많은 정보: <https://ngrok.com/docs/agent/cli/>.

- 지정된 포트로 로컬 HTTP 서비스 노출:

`ngrok http {{80}}`

- 특정 호스트에서 로컬 HTTP 서비스 노출:

`ngrok http {{foo.dev}}:{{80}}`

- 로컬 HTTPS 서버 노출:

`ngrok http https://localhost`

- 지정된 포트로 TCP 트래픽 노출:

`ngrok tcp {{22}}`

- 특정 호스트 및 포트를 위한 TLS 트래픽 노출:

`ngrok tls -hostname={{foo.com}} {{443}}`
