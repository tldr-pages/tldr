# crontab

> Programma cron job per essere eseguiti a determinati intervalli di tempo per l'utente corrente.
> Formato definizione di un job: "(minuto) (ora) (giorno_del_mese) (mese) (giorno_della_settimana) comando_da_eseguire".
> Maggiori informazioni: <https://crontab.guru/>.

- Modifica il file crontab per l'utente corrente:

`crontab -e`

- Elenca i cron job esistenti per l'utente corrente:

`crontab -l`

- Rimuovi tutti i cron job per l'utente corrente:

`crontab -r`

- Esempio di un job eseguito alle 10:00 ogni giorno (* vuol dire qualsiasi valore):

`0 10 * * * {{comando_da_eseguire}}`

- Esempio di un job eseguito ogni minuto il 3 Aprile:

`* * 3 Apr * {{comando_da_eseguire}}`

- Esempio di un job che esegue un determinato script alle 02:30 ogni venerdì:

`30 2 * * Fri {{/percorso/assoluto/allo/script.sh}}`
