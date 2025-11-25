# pct exec

> Launch a command inside a specified container.
> More information: <https://pve.proxmox.com/pve-docs/pct.1.html#cli_pct_exec>.

- Launch a command in a container:

`pct {{[ex|exec]}} {{100}} {{command}}`

- Open a Bash shell in a container:

`pct {{[ex|exec]}} {{100}} bash`

- Pass arguments to the command:

`pct {{[ex|exec]}} {{100}} -- {{command}} {{arguments}}`
