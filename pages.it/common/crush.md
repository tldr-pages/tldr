# crush

> Assistente da terminale basato su IA per attività di sviluppo software.
> Fornisce un'interfaccia di chat interattiva con funzionalità di intelligenza artificiale, analisi del codice e integrazione LSP.
> Maggiori informazioni: <https://github.com/charmbracelet/crush>.

- Avvia la modalità interattiva:

`crush`

- Esegui con log di debug attivi:

`crush {{[-d|--debug]}}`

- Esegui con log di debug in una directory specifica:

`crush {{[-d|--debug]}} {{[-c|--cwd]}} {{percorso/al/progetto}}`

- Esegui un prompt singolo in modalità non interattiva:

`crush run "{{Spiega l'uso del contesto in Go}}"`

- Esegui in modalità pericolosa (accetta automaticamente tutti i permessi):

`crush {{[-y|--yolo]}}`

- Mostra la versione:

`crush {{[-v|--version]}}`
