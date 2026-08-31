# pct clone

> Clona un container.
> Maggiori informazioni: <https://pve.proxmox.com/pve-docs/pct.1.html#cli_pct_clone>.

- Clona un container:

`pct {{[cl|clone]}} {{100}} {{101}}`

- Clona un container con un nome personalizzato:

`pct {{[cl|clone]}} {{100}} {{101}} --hostname {{nome_host}}`

- Crea un clone completo invece di un clone collegato:

`pct {{[cl|clone]}} {{100}} {{101}} --full`
