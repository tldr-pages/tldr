# at

> Esegue comandi una sola volta in un momento futuro.
> I risultati vengono inviati alla mail dell'utente.
> Maggiori informazioni: <https://manned.org/at>.

- Crea comandi interattivamente ed eseguili tra 5 minuti (premi `<Ctrl d>` quando finito):

`at now + 5 minutes`

- Crea comandi interattivamente ed eseguili a un orario specifico:

`at {{hh:mm}}`

- Esegue un comando da `stdin` alle 10:00 di oggi:

`echo "{{comando}}" | at 1000`

- Esegue comandi da un file specifico il prossimo martedì:

`at -f {{percorso/al/file}} 9:30 PM Tue`

- Elenca tutti i job in coda per l'utente corrente (uguale a `atq`):

`at -l`

- Visualizza un job specifico:

`at -c {{numero_job}}`
