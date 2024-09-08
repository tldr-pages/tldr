# apt-key

> Servizio di gestione delle chiavi per il gestore di pacchetti APT su Debian ed Ubuntu.
> Maggiori informazioni: <https://manpages.debian.org/latest/apt/apt-key.8.html>.

- Elenca le chiavi fidate:

`apt-key list`

- Aggiunge una chiave al portachiavi delle chiavi fidate:

`apt-key add {{file_chiave_pubblica.asc}}`

- Elimina una chiave dal portachiavi delle chiavi fidate:

`apt-key del {{id_chiave}}`

- Aggiunge una chiave remota al portachiavi delle chiavi fidate:

`wget -qO - {{https://indirizzo.tld/filename.key}} | apt-key add -`

- Aggiunge una chiave da un server di chiavi con il solo ID della chiave:

`apt-key adv --keyserver {{pgp.mit.edu}} --recv {{ID_DELLA_CHIAVE}}`
