# complete

> Fornisce autocompletamento per argomenti dei comandi della shell.
> Maggiori informazioni: <https://www.gnu.org/software/bash/manual/bash.html#index-complete>.

- Applica ad un comando una funzione per gestirne l'autocompletamento:

`complete -F {{funzione}} {{comando}}`

- Applica ad un comando un altro comando per gestirne l'autocompletamento:

`complete -C {{comando_per_autocompletamento}} {{comando}}`

- Applica l'autocompletamento senza aggiungere uno spazio dopo la parola completata:

`complete -o nospace -F {{function}} {{comando}}`
