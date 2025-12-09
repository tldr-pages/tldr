# caddy

> Go로 작성된 자동 HTTPS를 갖춘 엔터프라이즈급 오픈 소스 웹 서버.
> 더 많은 정보: <https://caddyserver.com/docs/command-line>.

- 포어그라운드에서 Caddy를 시작:

`caddy run`

- 지정된 Caddyfile로 Caddy를 시작:

`caddy run --config {{경로/대상/Caddyfile}}`

- 백그라운드에서 Caddy를 시작:

`caddy start`

- 백그라운드 Caddy 프로세스를 중지:

`caddy stop`

- 탐색 가능한 인터페이스를 사용하여 지정된 포트에서 간단한 파일 서버를 실행:

`caddy file-server --listen :{{8000}} --browse`

- 리버스 프록시 서버 실행:

`caddy reverse-proxy --from :{{80}} --to localhost:{{8000}}`
