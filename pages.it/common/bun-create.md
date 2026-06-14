# bun create

> Crea un nuovo progetto da un template.
> Maggiori informazioni: <https://bun.com/docs/runtime/templating/create>.

- Crea un nuovo progetto da un template ufficiale in modo interattivo:

`bun {{[c|create]}} {{template}}`

- Crea un nuovo progetto da un template ufficiale in una nuova directory:

`bun {{[c|create]}} {{template}} {{percorso/della/destinazione}}`

- Crea un nuovo progetto da un template di repository GitHub:

`bun {{[c|create]}} {{https://github.com/username/repo}} {{percorso/della/destinazione}}`

- Crea un nuovo progetto da un template locale:

`bun {{[c|create]}} {{percorso/del/template}} {{percorso/della/destinazione}}`

- Crea un nuovo progetto sovrascrivendo la directory di destinazione se esiste:

`bun {{[c|create]}} {{template}} {{percorso/della/destinazione}} --force`

- Crea un nuovo progetto senza inizializzare automaticamente un repository Git:

`bun {{[c|create]}} {{template}} {{percorso/della/destinazione}} --no-git`

- Crea un nuovo progetto senza installare automaticamente le dipendenze:

`bun {{[c|create]}} {{template}} {{percorso/della/destinazione}} --no-install`
