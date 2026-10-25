# pvesm

> Gestisce lo storage di Proxmox.
> Maggiori informazioni: <https://pve.proxmox.com/pve-docs/pvesm.1.html>.

- Mostra lo stato di tutti i datastore:

`pvesm {{[st|status]}}`

- Elenca i contenuti dello storage:

`pvesm {{[l|list]}} {{nome_storage}}`

- Mostra il percorso di un file archiviato:

`pvesm {{[pa|path]}} {{nome_storage}}:{{tipo_contenuto}}/{{nome_file}}`

- Aggiunge uno storage di tipo directory:

`pvesm {{[ad|add]}} dir {{nome_storage}} --path {{percorso/della/directory}}`

- Configura uno storage per contenere tipi di contenuto specifici:

`pvesm {{[se|set]}} {{nome_storage}} --content {{iso,images,backup,vztmpl,rootdir,snippets,import}}`

- Elimina un file dallo storage:

`pvesm {{[f|free]}} {{local:iso/archlinux-2025.08.01-x86_64.iso}}`

- Rimuove uno storage:

`pvesm {{[r|remove]}} {{nome_storage}}`
