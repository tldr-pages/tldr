# tailscale ssh

> SSH到Tailscale机器（仅限Linux）。
> 更多信息：<https://tailscale.com/kb/1193/tailscale-ssh>。

- 在主机上宣传/禁用SSH：

`sudo tailscale up --ssh={{true|false}}`

- SSH到启用了Tailscale-SSH的特定主机：

`tailscale ssh {{username}}@{{host}}`