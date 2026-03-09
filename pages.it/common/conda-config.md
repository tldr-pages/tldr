# conda config

> Modifica valori di configurazione in `.condarc`.
> Maggiori informazioni: <https://docs.conda.io/projects/conda/en/latest/commands/config.html>.

- Mostra tutte le configurazioni:

`conda config --show`

- Mostra valore configurazione specifica:

`conda config --show {{opzione_config}}`

- Imposta valore configurazione:

`conda config --set {{chiave}} {{valore}}`

- Rimuove valore configurazione:

`conda config --remove {{chiave}} {{valore}}`

- Aggiunge valore a lista configurazione:

`conda config --append {{chiave}} {{valore}}`

- Inserisce valore all'inizio lista:

`conda config --prepend {{chiave}} {{valore}}`

- Descrive opzione configurazione:

`conda config --describe {{opzione_config}}`
