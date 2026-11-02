# pve-firewall

> Gestisce il firewall di Proxmox VE.
> Maggiori informazioni: <https://pve.proxmox.com/wiki/Firewall>.

- Compila e stampa tutte le regole del firewall:

`pve-firewall {{[c|compile]}}`

- Mostra informazioni sulla rete locale:

`pve-firewall {{[l|localnet]}}`

- Riavvia il servizio firewall di Proxmox VE:

`pve-firewall {{[r|restart]}}`

- Avvia il servizio firewall di Proxmox VE:

`pve-firewall start`

- Ferma il servizio firewall di Proxmox VE:

`pve-firewall stop`

- Simula tutte le regole del firewall:

`pve-firewall {{[si|simulate]}}`

- Mostra lo stato del firewall di Proxmox VE:

`pve-firewall status`
