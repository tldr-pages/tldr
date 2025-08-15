# pct set

> Set container options.
> More information: <https://pve.proxmox.com/pve-docs/pct.1.html>.

- Set container to start automatically on boot:

`pct set {{100}} --onboot`

- Set a container to have a static IP:

`pct set {{100}} --net0 name=eth0,bridge=vmbr0,ip={{10.0.0.100/24}},gw={{10.0.0.1}}`

- Set container memory limit:

`pct set {{100}} --memory {{8192}}`
