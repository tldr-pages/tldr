# btrfs filesystem

> Gestisce i filesystem btrfs.
> Maggiori informazioni: <https://btrfs.readthedocs.io/en/latest/btrfs-filesystem.html>.

- Mostra l'utilizzo del filesystem (opzionalmente esegui come root per informazioni dettagliate):

`btrfs {{[f|filesystem]}} {{[u|usage]}} {{percorso/al/mount_btrfs}}`

- Mostra l'utilizzo per dispositivi individuali:

`sudo btrfs {{[f|filesystem]}} {{[sh|show]}} {{percorso/al/mount_btrfs}}`

- Deframmenta un singolo file su un filesystem btrfs (evita durante l'esecuzione di un agente di deduplicazione):

`sudo btrfs {{[f|filesystem]}} {{[de|defragment]}} {{[-v|--verbose]}} {{percorso/al/file}}`

- Deframmenta una directory ricorsivamente (non attraversa i confini dei sottovolumi):

`sudo btrfs {{[f|filesystem]}} {{[de|defragment]}} {{[-v|--verbose]}} -r {{percorso/della/directory}}`

- Forza la sincronizzazione dei blocchi dati non scritti su disco(i):

`sudo btrfs {{[f|filesystem]}} {{[sy|sync]}} {{percorso/al/mount_btrfs}}`

- Riassume l'utilizzo del disco per i file in una directory ricorsivamente:

`sudo btrfs {{[f|filesystem]}} du {{[-s|--summarize]}} {{percorso/della/directory}}`

- Crea un file di swap:

`sudo btrfs {{[f|filesystem]}} {{[m|mkswapfile]}} --size {{8g}} --uuid {{clear|random|time|UUID_value}} {{percorso/allo/swapfile}}`
