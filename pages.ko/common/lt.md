# lt

> Localtunnel은 로컬호스트를 외부에 노출시켜 손쉽게 테스트하고 공유할 수 있게 해줍니다.
> 더 많은 정보: <https://github.com/localtunnel/localtunnel>.

- 특정 포트에서 터널 시작:

`lt --port {{8000}}`

- 포워딩을 수행하는 업스트림 서버 지정:

`lt --port {{8000}} --host {{호스트}}`

- 특정 서브도메인 요청:

`lt --port {{8000}} --subdomain {{서브도메인}}`

- 기본 요청 정보 출력:

`lt --port {{8000}} --print-requests`

- 기본 웹 브라우저에서 터널 URL 열기:

`lt --port {{8000}} --open`
