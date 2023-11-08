# amass track

> Houd verschillen bij tussen opsommingen van hetzelfde domein.
> Meer informatie: <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-track-subcommand>.

- Laat het verschil zien tussen de laatste twee opsommingen van een specifiek domein:

`amass track -dir {{pad/naar/database_map}} -d {{domeinnaam}} -last 2`

- Laat het verschil zien tussen een specitiek tijdstip en de laatste opsomming:

`amass track -dir {{pad/naar/database_map}} -d {{domeinnaam}} -since {{01/02 15:04:05 2006 MST}}`
