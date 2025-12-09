# aptitude

> Utilità di gestione pacchetti per Debian e Ubuntu.
> Maggiori informazioni: <https://manned.org/aptitude>.

- Sincronizza l'elenco dei pacchetti e delle versioni disponibili. Va eseguito prima di altri comandi `aptitude`:

`sudo aptitude update`

- Installa un nuovo pacchetto e le sue dipendenze:

`sudo aptitude install {{package}}`

- Cerca un pacchetto:

`aptitude search {{package}}`

- Cerca un pacchetto installato (`?installed` è un termine di ricerca di `aptitude`):

`aptitude search '?installed({{package}})'`

- Rimuove un pacchetto e tutti i pacchetti che dipendono da esso:

`sudo aptitude remove {{package}}`

- Aggiorna i pacchetti installati alle versioni più recenti disponibili:

`sudo aptitude upgrade`

- Aggiorna i pacchetti installati (come `aptitude upgrade`) inclusa la rimozione di pacchetti obsoleti e l'installazione di pacchetti aggiuntivi per soddisfare nuove dipendenze:

`sudo aptitude full-upgrade`

- Mettere in pausa un pacchetto installato per impedirne l'aggiornamento automatico:

`sudo aptitude hold '?installed({{package}})'`
