# apt-get

> Servizio di gestione dei pacchetti per Debian e Ubuntu
> Cerca i pacchetti usando `apt-cache`.

- Aggiorna la lista dei pacchetti e delle loro versioni disponibili (è consigliato eseguire questo comando prima di altri comandi `apt-get`):

`apt-get update`

- Installa un pacchetto, o lo aggiorna all'ultima versione disponibile:

`apt-get install {{pacchetto}}`

- Rimuove un pacchetto:

`apt-get remove {{pacchetto}}`

- Rimuove un pacchetto ed i suoi file di configurazione:

`apt-get purge {{pacchetto}}`

- Aggiorna tutti i pacchetti installati alla versione disponibile più recente:

`apt-get upgrade`

- Pulisce gli archivi locali - rimuovendo i file (.deb) da scaricamenti interrotti che non possono più essere scaricati:

`apt-get autoclean`

- Rimuove tutti i pacchetti che non sono più necessari:

`apt-get autoremove`

- Aggiorna tutti i pacchetti installati (come `upgrade`), rimuovendo i pacchetti obsoleti ed installando ulteriori pacchetti per soddisfare le nuove dipendenze:

`apt-get dist-upgrade`
