# warp-cli

> Cloudflare의 WARP 서비스에 대한 연결을 연결, 연결 해제하고 모드를 전환.
> WARP는 개인정보 보호, 보안, 속도를 위해 트래픽을 암호화하는 VPN입니다.
> 같이 보기: `fastd`, `ivpn`, `mozillavpn`, `mullvad`.
> 더 많은 정보: <https://developers.cloudflare.com/warp-client/>.

- 현재 장치를 WARP에 등록 (첫 연결 전에 실행 필요):

`warp-cli registration new`

- WARP에 연결:

`warp-cli connect`

- WARP에서 연결 해제:

`warp-cli disconnect`

- WARP 연결 상태 표시:

`warp-cli status`

- 특정 모드로 전환:

`warp-cli set-mode {{모드}}`

- 도움말 표시:

`warp-cli help`

- 하위 명령에 대한 도움말 표시:

`warp-cli help {{하위_명령}}`
