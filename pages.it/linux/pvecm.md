# pvecm

> Cluster Manager di Proxmox VE.
> Maggiori informazioni: <https://pve.proxmox.com/pve-docs/pvecm.1.html>.

- Aggiunge il nodo corrente a un cluster esistente:

`pvecm add {{hostname_o_ip}}`

- Aggiunge un nodo alla configurazione del cluster (uso interno):

`pvecm {{[addn|addnode]}} {{nodo}}`

- Mostra la versione dell'API di join del cluster disponibile su questo nodo:

`pvecm {{[ap|apiver]}}`

- Genera una nuova configurazione del cluster:

`pvecm {{[c|create]}} {{nomecluster}}`

- Rimuove un nodo dalla configurazione del cluster:

`pvecm {{[d|delnode]}} {{nodo}}`

- Mostra la vista locale dei nodi del cluster:

`pvecm {{[n|nodes]}}`

- Mostra la vista locale dello stato del cluster:

`pvecm {{[s|status]}}`
