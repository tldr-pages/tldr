# tailscale up

> 클라이언트를 Tailscale 네트워크에 연결.
> 버전 1.8 이상에서는 명령줄 인수가 저장되어 덮어쓰거나 `--reset`을 호출할 때까지 재사용됩니다.
> 더 많은 정보: <https://tailscale.com/kb/1080/cli/#up>.

- Tailscale에 연결:

`sudo tailscale up`

- 연결하고 현재 기기를 인터넷 트래픽의 종료 노드로 제공:

`sudo tailscale up --advertise-exit-node`

- 특정 노드를 인터넷 트래픽을 위한 종료 노드로 사용하여 연결:

`sudo tailscale up --exit-node={{종료_노드_IP}}`

- 연결하고 현재 노드로의 수신 연결 차단:

`sudo tailscale up --shields-up`

- 연결하고 관리자 패널의 DNS 구성을 수락하지 않음 (기본값은 `true`):

`sudo tailscale up --accept-dns=false`

- 연결하고 Tailscale을 서브넷 라우터로 구성:

`sudo tailscale up --advertise-routes={{10.0.0.0/24,10.0.1.0/24,...}}`

- 연결하고 Tailscale에서 서브넷 경로 수락:

`sudo tailscale up --accept-routes`

- 지정되지 않은 설정을 기본값으로 재설정하고 연결:

`sudo tailscale up --reset`
