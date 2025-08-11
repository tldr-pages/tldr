# pct exec

> Launch a command inside a specified container.
> More information: <https://pve.proxmox.com/pve-docs/pct.1.html>.

- Launch a command in a container:

`pct {{[ex|exec]}} {{100}} {{command}}`

- Open a bash shell in a container:

`pct {{[ex|exec]}} {{100}} bash`

- Pass arguments to the command:

`pct {{[ex|exec]}} {{100}} -- {{command}} {{arguments}}`
