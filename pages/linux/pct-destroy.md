# pct destroy

> Destroy a container.
> More information: <https://pve.proxmox.com/pve-docs/pct.1.html#cli_pct_destroy>.

- Destroy a container:

`pct {{[des|destroy]}} {{container_id}}`

- Destroy a container even if it's running:

`pct {{[des|destroy]}} {{container_id}} --force`

- Also delete all references to this container:

`pct {{[des|destroy]}} {{container_id}} --purge`
