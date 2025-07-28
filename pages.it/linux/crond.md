# crond

> Servizio per eseguire i comandi pianificati dai file crontab.
> Più informazioni: <https://manned.org/crond>.

- Avvia un servizio in background e controlla i comandi pianificati:

`crond`

- Avvia un servizio in primo piano e controlla i comandi pianificati:

`crond -n`

- Invia l'output del job dal servizio al [s]ystem log:

`crond -s`

- Sovrascrive le limitazione di default e accetta crontables personalizzate:

`crond -p`

- Eredita il percorso del file crontab dalle impostazioni dell'ambiente:

`crond -P`
