# tailscale ssh

> SSH to a Tailscale machine (Linux Only).
> More information: <https://tailscale.com/kb/1193/tailscale-ssh>.

- Advertise/Disable SSH on the host:

`sudo tailscale up --ssh={{true|false}}`

- SSH to a host which has Tailscale-SSH enabled:

`tailscale ssh {{user}}@{{host}}`
