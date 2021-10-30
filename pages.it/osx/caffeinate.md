# caffeinate

> Impedisci al mac di sospendersi.
> Maggiori informazioni: <https://ss64.com/osx/caffeinate.html>.

- Impedisci la sospensione per un'ora (3600 secondi):

`caffeinate -u -t {{3600}}`

- Impedisci la sospensione fino al completamento dell'esecuzione di un comando:

`caffeinate -s {{comando}}`

- Impedisci la sospensione fino alla pressione della combinazione di tasti Ctrl-C:

`caffeinate -i`
