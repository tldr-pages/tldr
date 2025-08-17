# abrt-cli

> Automatisch bug rapportage hulpmiddel voor Fedora-gebaseerde systemen.
> Gebruikt om applicatie crashes te detecteren, analyseren en rapporteren.
> Meer informatie: <https://abrt.readthedocs.io/en/latest/usage.html>.

- Lijst van gedetecteerde problemen:

`abrt-cli list`

- Toon details van een specifiek probleem:

`abrt-cli info {{probleem_id}}`

- Een crashrapport verwijderen:

`abrt-cli remove {{probleem_id}}`

- Een probleem rapporteren aan de geconfigureerde bugtracker (bijv. Bugzilla):

`abrt-cli report {{probleem_id}}`

- Een logbestand monitoren en een programma starten als er een overeenkomst wordt gevonden:

`abrt-watch-log -F {{error_string}} {{/var/log/myapp.log}} {{notify-send “Crash gedetecteerd”}}`

- Genereer handmatig een rapport om te debuggen:

`abrt-cli report {{[-a|--analyze]}} {{probleem_id}}`
