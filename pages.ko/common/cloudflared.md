# cloudflared

> Cloudflare 네트워크에 대한 지속적인 연결을 생성.
> 더 많은 정보: <https://developers.cloudflare.com/argo-tunnel/>.

- Cloudflare 계정의 도메인에 대한 연결을 인증하고 연결:

`cloudflared tunnel login`

- 특정 이름의 터널을 생성:

`cloudflared tunnel create {{이름}}`

- 로컬 서버에서 Cloudflare의 호스트로 터널을 설정:

`cloudflared tunnel --hostname {{호스트명}} localhost:{{port_number}}`

- 로컬 서버의 인증서를 확인하지 않고, 로컬 서버에서 Cloudflare의 호스트로 터널을 설정:

`cloudflared tunnel --hostname {{호스트명}} localhost:{{포트_번호}} --no-tls-verify`

- 로그를 파일에 저장:

`cloudflared tunnel --hostname {{호스트명}} http://localhost:{{포트_번호}} --loglevel {{panic|fatal|error|warn|info|debug}} --logfile {{경로/대상/파일}}`

- cloudflared를 시스템 서비스로 설치:

`cloudflared service install`
