# conda config

> Modifica i valori di configurazione nel file `.condarc`.
> Maggiori informazioni: <https://docs.conda.io/projects/conda/en/latest/commands/config.html>.

- Mostra tutti i valori di configurazione:

`conda config --show`

- Mostra il valore corrente di un'opzione di configurazione:

`conda config --show {{opzione_configurazione}}`

- Imposta un valore di configurazione:

`conda config --set {{chiave}} {{valore}}`

- Rimuovi un valore di configurazione:

`conda config --remove {{chiave}} {{valore}}`

- Aggiungi un valore in coda a una lista di una chiave di configurazione esistente:

`conda config --append {{chiave}} {{valore}}`

- Aggiungi un valore all’inizio di una lista di una chiave di configurazione esistente:

`conda config --prepend {{chiave}} {{valore}}`

- Descrivi l'opzione di configurazione specificata:

`conda config --describe {{opzione_configurazione}}`
