# apt-get

> Servizio di gestione dei pacchetti per Debian e Ubuntu.
> Cerca i pacchetti usando `apt-cache`.
> Maggiori informazioni: <https://manned.org/apt-get.8>.

- Aggiorna la lista dei pacchetti e delle loro versioni disponibili (è consigliato eseguire questo comando prima di altri comandi `apt-get`):

`sudo apt-get update`

- Installa un pacchetto, o lo aggiorna all'ultima versione disponibile:

`sudo apt-get install {{pacchetto}}`

- Rimuove un pacchetto:

`sudo apt-get remove {{pacchetto}}`

- Rimuove un pacchetto ed i suoi file di configurazione:

`sudo apt-get purge {{pacchetto}}`

- Aggiorna tutti i pacchetti installati alla versione disponibile più recente:

`sudo apt-get upgrade`

- Pulisce gli archivi locali - rimuovendo i file (.deb) da scaricamenti interrotti che non possono più essere scaricati:

`apt-get autoclean`

- Rimuove tutti i pacchetti che non sono più necessari:

`sudo apt-get autoremove`

- Aggiorna tutti i pacchetti installati (come `upgrade`), rimuovendo i pacchetti obsoleti ed installando ulteriori pacchetti per soddisfare le nuove dipendenze:

`sudo apt-get dist-upgrade`
