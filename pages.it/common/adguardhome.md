# AdGuardHome

> Software di rete per bloccare ads e tracciamento.
> Maggiori informazioni: <https://github.com/AdguardTeam/AdGuardHome>.

- Avvia AdGuard Home:

`AdGuardHome`

- Specifica un file di configurazione:

`AdGuardHome --config {{percorso/AdGuardHome.yaml}}`

- Memorizza i dati in una directory di lavoro specifica:

`AdGuardHome --work-dir {{percorso/della/directory}}`

- Installa o disinstalla AdGuard Home come servizio:

`AdGuardHome --service {{install|uninstall}}`

- Avvia il servizio AdGuard Home:

`AdGuardHome --service start`

- Ricarica la configurazione per il servizio AdGuard Home:

`AdGuardHome --service reload`

- Ferma o riavvia il servizio AdGuard Home:

`AdGuardHome --service {{stop|restart}}`
