# pct exec

> Esegue un comando all'interno di un container specificato.
> Maggiori informazioni: <https://pve.proxmox.com/pve-docs/pct.1.html#cli_pct_exec>.

- Esegue un comando in un container:

`pct {{[ex|exec]}} {{100}} {{comando}}`

- Apre una shell Bash in un container:

`pct {{[ex|exec]}} {{100}} bash`

- Passa argomenti al comando:

`pct {{[ex|exec]}} {{100}} -- {{comando}} {{argomenti}}`
