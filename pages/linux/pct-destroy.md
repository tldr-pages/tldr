# pct destroy

> Destroy a container.
> More information: <https://pve.proxmox.com/pve-docs/pct.1.html>.

- Destroy a container:

`pct {{[des|destroy]}} {{100}}`

- Destroy a container even if it's running:

`pct {{[des|destroy]}} {{100}} --force`

- Also delete all references to this container:

`pct {{[des|destroy]}} {{100}} --purge`
