# tailscale funnel

> Tailscale을 사용하여 로컬 서버를 인터넷에 공개.
> 더 많은 정보: <https://tailscale.com/kb/1311/tailscale-funnel>.

- 로컬 파일 또는 디렉터리를 포그라운드에서 공개:

`tailscale funnel {{path/to/file_or_directory}}`

- 127.0.0.1:3000에서 실행 중인 HTTP 서버를 포그라운드에서 공개:

`tailscale funnel 3000`

- 127.0.0.1:3000에서 실행 중인 HTTP 서버를 백그라운드에서 공개:

`tailscale funnel --bg 3000`

- 유효하지 않거나 자체 서명된 인증서를 사용하는 <https://localhost:8443>의 HTTPS 서버를 공개:

`tailscale funnel https+insecure://localhost:8443`
