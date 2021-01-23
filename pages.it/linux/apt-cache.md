# apt-cache

> Strumenti di Debian e Ubuntu per richiedere informazioni sui pacchetti.

- Cerca un pacchetto nelle sorgenti attuali:

`apt-cache search {{query}}`

- Mostra informazioni su un pacchetto:

`apt-cache show {{pacchetto}}`

- Mostra se un pacchetto è installato ed aggiornato:

`apt-cache policy {{pacchetto}}`

- Mostra le dipendenze di un pacchetto:

`apt-cache depends {{pacchetto}}`

- Mostra i pacchetti che dipendono da un particolare pacchetto:

`apt-cache rdepends {{pacchetto}}`
