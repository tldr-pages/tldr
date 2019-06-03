# browser-sync

> Avvia un web-server locale che si aggiorna al cambiamento dei file.
> Maggiori informazioni: <https://browsersync.io/docs/command-line>.

- Avvia un server da una specifica directory:

`browser-sync start --server {{percorso/a/directory}} --files {{percorso/a/directory}}`

- Avvia un server da una directory locale, monitorando tutti i file CSS:

`browser-sync start --server --files '{{percorso/a/directory/*.css}}'`

- Crea un file di configurazione:

`browser-sync init`

- Avvia bower-sync da un file di configurazione:

`browser-sync start --config {{file_di_configurazione}}`
