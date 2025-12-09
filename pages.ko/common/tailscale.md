# tailscale

> 개인 WireGuard 네트워크 서비스.
> `up`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
> 더 많은 정보: <https://tailscale.com/kb/1080/cli>.

- Tailscale에 연결:

`sudo tailscale up`

- Tailscale에서 연결 해제:

`sudo tailscale down`

- 현재 Tailscale IP 주소 표시:

`tailscale ip`

- Tailscale 계층에서 피어 노드를 핑하고 각 응답에 대한 경로 표시:

`tailscale ping {{IP|호스트명}}`

- 로컬 네트워크 상태를 분석하고 결과 표시:

`tailscale netcheck`

- Tailscale을 제어하기 위한 웹 서버 시작:

`tailscale web`

- 문제 진단을 돕기 위한 공유 가능한 식별자 표시:

`tailscale bugreport`

- 하위 명령에 대한 도움말 표시:

`tailscale {{하위_명령}} --help`
