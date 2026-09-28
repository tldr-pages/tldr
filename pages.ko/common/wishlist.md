# wishlist

> SSH 디렉터리이며 멀티플렉서.
> SSH 서버 또는 Wish 애플리케이션에 연결하기 위한 단일 진입점 역할.
> 더 많은 정보: <https://github.com/charmbracelet/wishlist>.

- `~/.ssh/config` 파일에 등록된 SSH 서버를 탐색 (로컬 모드):

`wishlist`

- 원격 접속을 제공하도록 Wishlist를 서버 모드로 시작:

`wishlist {{[s|serve]}}`

- 사용자 지정 설정 파일 사용:

`wishlist {{[-c|--config]}} {{경로/대상/설정파일.yaml}}`

- Zeroconf (mDNS/Bonjour)를 사용하여 SSH 엔드포인트 검색:

`wishlist --zeroconf.enabled`

- DNS SRV 레코드에서 SSH 노드 검색:

`wishlist --srv.domain {{example.com}}`

- Tailscale tailnet에서 SSH 노드 검색:

`wishlist --tailscale.net={{tailnet_이름}} --tailscale.key={{tskey-api-abc123}}`
