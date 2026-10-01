# aureport

> Genereer samenvattende rapporten van auditd-logs.
> Meer informatie: <https://manned.org/aureport>.

- Toon een samenvatting van auditd-gebeurtenissen:

`sudo aureport`

- Genereer een samenvatting van inloggebeurtenissen:

`sudo aureport {{[-l|--login]}}`

- Toon alle syscall-rapporten:

`sudo aureport {{[-s|--syscall]}}`

- Genereer een samenvatting van uitvoerbare-bestand-gebeurtenissen:

`sudo aureport {{[-x|--executable]}}`

- Toon een samenvatting van gebeurtenissen voor een specifieke periode:

`sudo aureport {{[-ts|--start]}} {{starttijd}} {{[-te|--end]}} {{eindtijd}}`

- Toon alle auditbestanden en de periode van gebeurtenissen die ze bestrijken:

`sudo aureport {{[-t|--log-time]}}`

- Toon de help:

`aureport --help`
