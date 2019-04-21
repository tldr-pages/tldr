# cradle sql

> Gestisci database SQL di Cradle.

- Ricostruisci lo schema del database:

`cradle sql build`

- Ricostruisci lo schema del database per uno specifico pacchetto:

`cradle sql build {{nome_pacchetto}}`

- Svuota l'intero database:

`cradle sql flush`

- Svuota le tabelle del database per uno specifico pacchetto:

`cradle sql flush {{nome_pacchetto}}`

- Popola le tabelle per tutti i pacchetti:

`cradle sql populate`

- Popola le tabelle per uno specifico pacchetto:

`cradle sql populate {{nome_pacchetto}}`
