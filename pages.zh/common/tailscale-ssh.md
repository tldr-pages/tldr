# tailscale ssh

> 通过 Tailscale SSH 到 Tailscale 机器（仅限 Linux）。
> 更多信息：<https://tailscale.com/kb/1193/tailscale-ssh>.

- 在主机上启用/禁用 SSH：

`tailscale up --ssh={{true|false}}`

- SSH 到启用了 Tailscale-SSH 的特定主机：

`tailscale ssh {{username}}@{{host}}`