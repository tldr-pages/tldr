# cradle sql

> Management von Cradle SQL Datenbanken.
> Mehr Informationen: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#sql>.

- Neu-Generierung eines Datenbank Schemas:

`cradle sql build`

- Neu-Generierung eines Datenbank Schemas für ein bestimmtes Paket:

`cradle sql build {{Paket}}`

- Entleeren der gesamten Datenbank:

`cradle sql flush`

- Entleeren der Datenbank für ein bestimmtes Paket:

`cradle sql flush {{Paket}}`

- Befüllung der Tabellen für alle Pakete:

`cradle sql populate`

- Befüllung der Tabellen für ein bestimmtes Paket:

`cradle sql populate {{Paket}}`
