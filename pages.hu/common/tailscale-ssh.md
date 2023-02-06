# tailscale ssh

> SSH egy Tailscale géphez (csak Linux). További információ: <https://tailscale.com/kb/1193/tailscale-ssh>.

- Az SSH hirdetése/letiltása az állomáson:

`sudo tailscale up --ssh={{true|false}}`

- SSH egy adott állomáshoz, amelyen engedélyezve van a Tailscale-SSH:

`tailscale ssh {{username}}@{{host}}`
