# AdGuardHome

> Netwerkbrede software voor het blokkeren van advertenties en tracking.
> Meer informatie: <https://github.com/AdguardTeam/AdGuardHome>.

- Voer AdGuard Home uit:

`AdGuardHome`

- Voer AdGuard Home uit met een specifieke configuratie:

`AdGuardHome --config {{pad/naar/AdGuardHome.yaml}}`

- Stel de werkmap in waarin gegevens moeten worden opgeslagen:

`AdGuardHome --work-dir {{pad/naar/map}}`

- Installeer of verwijder AdGuard Home als een service:

`AdGuardHome --service {{install|uninstall}}`

- Start de AdGuard Home-service:

`AdGuardHome --service start`

- Laad de configuratie voor de AdGuard Home-service opnieuw:

`AdGuardHome --service reload`

- Stop of herstart de AdGuard Home-service:

`AdGuardHome --service {{stop|restart}}`
