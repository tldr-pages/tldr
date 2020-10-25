# apt

> Servizio di gestione dei pacchetti per distribuzioni basate su Debian.
> Rimpiazzo raccomandato di apt-get quando usato interattivamente su Ubuntu 16.04 e versioni successive.

- Aggiorna la lista dei pacchetti e delle loro versioni disponibili (prima di altri comandi `apt` è consigliato eseguire questo comando):

`sudo apt update`

- Cerca per un dato pacchetto:

`apt search {{pacchetto}}`

- Mostra le informazioni su un pacchetto:

`apt show {{pacchetto}}`

- Installa un pacchetto, o lo aggiorna all'ultima versione disponibile:

`sudo apt install {{pacchetto}}`

- Rimuove un pacchetto (usando `purge` rimuove anche i suoi file di configurazione):

`sudo apt remove {{pacchetto}}`

- Aggiorna tutti i pacchetti installati alla più nuova versione disponibile:

`sudo apt upgrade`

- Elenca tutti i pacchetti:

`apt list`

- Elenca i pacchetti installati:

`apt list --installed`
