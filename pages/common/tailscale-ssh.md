# tailscale ssh

> SSH to a Tailscale machine (Linux Only).
> More information: <https://tailscale.com/kb/1193/tailscale-ssh>.

- Advertise SSH on the host:

`sudo tailscale up --ssh=true`

- Disable SSH on the host:

`sudo tailscaleSSH to a Tailscale machine (Linux Only). up --ssh=false`

- SSH to a host which has Tailscale-SSH enabled:

`tailscale ssh {{user}}@{{host}}`
