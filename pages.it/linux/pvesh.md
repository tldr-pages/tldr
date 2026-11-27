# pvesh

> Interfaccia con l'API di Proxmox VE.
> Maggiori informazioni: <https://pve.proxmox.com/pve-docs/pvesh.1.html>.

- Elenca i nodi disponibili:

`pvesh {{[g|get]}} /nodes`

- Mostra informazioni dettagliate su container o macchine virtuali:

`pvesh {{[g|get]}} /nodes/{{nome_nodo}}/{{lxc|qemu}}`

- Scopri i percorsi API:

`pvesh {{[l|ls]}} {{/}}`

- Mostra le istruzioni di utilizzo del percorso API:

`pvesh {{[u|usage]}} {{/pools}}`

- Aggiungi un nuovo thinpool a Proxmox:

`pvesh create /storage --storage {{id_archivio}} --vgname {{volume_group}} --type lvmthin --thinpool {{nome_thinpool}} --content {{tipo_contenuto1,tipo_contenuto2,...}}`
