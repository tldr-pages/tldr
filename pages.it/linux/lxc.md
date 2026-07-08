# lxc

> Gestisce i container Linux usando l'API REST lxd.
> Qualsiasi nome di container o pattern può essere preceduto dal nome di un server remoto.
> Maggiori informazioni: <https://manned.org/lxc>.

- Elenca i container locali che corrispondono a una stringa. Ometti la stringa per elencare tutti i container locali:

`lxc list {{match_string}}`

- Elenca le immagini che corrispondono a una stringa. Ometti la stringa per elencare tutte le immagini:

`lxc image list [{{remote}}:]{{match_string}}`

- Crea un nuovo container da un'immagine:

`lxc init [{{remote}}:]{{image}} {{container}}`

- Avvia un container:

`lxc start [{{remote}}:]{{container}}`

- Ferma un container:

`lxc stop [{{remote}}:]{{container}}`

- Mostra informazioni dettagliate su un container:

`lxc info [{{remote}}:]{{container}}`

- Crea uno snapshot di un container:

`lxc snapshot [{{remote}}:]{{container}} {{snapshot}}`

- Esegue un comando specifico all'interno di un container:

`lxc exec [{{remote}}:]{{container}} {{command}}`
