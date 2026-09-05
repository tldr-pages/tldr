# pct config

> Mostra la configurazione di un container.
> Maggiori informazioni: <https://pve.proxmox.com/pve-docs/pct.1.html#cli_pct_config>.

- Mostra la configurazione salvata:

`pct config {{100}}`

- Mostra la configurazione in esecuzione senza modifiche in sospeso:

`pct config {{100}} --current`

- Mostra la configurazione di uno snapshot specifico:

`pct config {{100}} --snapshot {{nome_snapshot}}`
