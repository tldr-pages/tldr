# cradle sql

> Verwalte Cradle SQL Datenbanken.
> Weitere Informationen: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#sql>.

- Generiere ein neues Datenbank-Schema:

`cradle sql build`

- Generiere ein neues Datenbank-Schema für ein bestimmtes Paket:

`cradle sql build {{paket}}`

- Entleere die gesamte Datenbank:

`cradle sql flush`

- Entleere die Datenbank für ein bestimmtes Paket:

`cradle sql flush {{paket}}`

- Befülle die Tabellen für alle Pakete:

`cradle sql populate`

- Befülle die Tabellen für ein bestimmtes Paket:

`cradle sql populate {{paket}}`
