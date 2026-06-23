# bun link

> Registra un pacchetto locale come collegabile oppure collega un pacchetto registrato in un progetto.
> Vedi anche: `bun unlink`.
> Maggiori informazioni: <https://bun.com/docs/pm/cli/link>.

- Collega il pacchetto corrente globalmente:

`bun link`

- Collega un pacchetto localmente in un progetto:

`bun link {{package_name}}`

- Collega un pacchetto in una directory specifica:

`bun link --cwd {{path/to/package}}`

- Esegui una simulazione senza collegare realmente:

`bun link --dry-run`

- Mostra l'help:

`bun link {{[-h|--help]}}`
