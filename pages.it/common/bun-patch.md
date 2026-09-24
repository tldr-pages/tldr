# bun patch

> Prepara un pacchetto per la patch o genera un file di patch.
> Maggiori informazioni: <https://bun.com/docs/pm/cli/patch>.

- Prepara un pacchetto per la patch:

`bun patch {{package}}`

- Prepara una versione specifica di un pacchetto:

`bun patch {{package}}@{{version}}`

- Prepara un pacchetto situato in un percorso specifico:

`bun patch {{path/to/package}}`

- Genera un file di patch per le modifiche apportate a un pacchetto:

`bun patch --commit {{path/to/package}}`

- Genera un file di patch e salvalo in una directory personalizzata:

`bun patch --commit {{path/to/package}} --patches-dir {{path/to/directory}}`
