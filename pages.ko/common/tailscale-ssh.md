# tailscale ssh

> Tailscale 머신에 SSH 접속 (리눅스 전용).
> 더 많은 정보: <https://tailscale.com/kb/1193/tailscale-ssh>.

- 호스트에서 SSH 광고/비활성화:

`sudo tailscale up --ssh={{true|false}}`

- Tailscale-SSH가 활성화된 특정 호스트에 SSH 접속:

`tailscale ssh {{사용자명}}@{{호스트}}`
