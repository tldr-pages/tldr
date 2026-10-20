# pvesm

> Gestisce l'archiviazione di Proxmox.
> Maggiori informazioni: <https://pve.proxmox.com/pve-docs/pvesm.1.html>.

- Ottieni lo stato per tutti i datastore:

`pvesm {{[st|status]}}`

- Elenca i contenuti dell'archivio:

`pvesm {{[l|list]}} {{nome_archivio}}`

- Aggiungi un archivio di directory:

`pvesm add {{[d|dir]}} {{nome_archivio}} --path {{percorso/directory}}`

- Imposta un archivio per contenere contenuti specifici:

`pvesm set {{nome_archivio}} --content {{iso,images,backup,vztmpl,...}}`

- Elimina un file dall'archivio:

`pvesm free {{local:iso/archlinux-2025.08.01-x86_64.iso}}`

- Rimuovi un archivio:

`pvesm {{[r|remove]}} {{nome_archivio}}`
