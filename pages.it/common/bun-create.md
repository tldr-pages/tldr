# bun create

> Crea un nuovo progetto da un template.
> Maggiori informazioni: <https://bun.com/docs/runtime/templating/create>.

- Crea un nuovo progetto da un template ufficiale in modo interattivo:

`bun {{[c|create]}} {{template}}`

- Crea un nuovo progetto da un template ufficiale in una nuova directory:

`bun {{[c|create]}} {{template}} {{path/to/destination}}`

- Crea un nuovo progetto da un template di repository GitHub:

`bun {{[c|create]}} {{https://github.com/username/repo}} {{path/to/destination}}`

- Crea un nuovo progetto da un template locale:

`bun {{[c|create]}} {{path/to/template}} {{path/to/destination}}`

- Crea un nuovo progetto sovrascrivendo la directory di destinazione se esiste:

`bun {{[c|create]}} {{template}} {{path/to/destination}} --force`

- Crea un nuovo progetto senza inizializzare automaticamente un repository Git:

`bun {{[c|create]}} {{template}} {{path/to/destination}} --no-git`

- Crea un nuovo progetto senza installare automaticamente le dipendenze:

`bun {{[c|create]}} {{template}} {{path/to/destination}} --no-install`
