# cradle sql

> Gestisci database SQL di Cradle.
> Maggiori informazioni: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#sql>.

- Ricostruisci lo schema del database:

`cradle sql build`

- Ricostruisci lo schema del database per uno specifico pacchetto:

`cradle sql build {{pacchetto}}`

- Svuota l'intero database:

`cradle sql flush`

- Svuota le tabelle del database per uno specifico pacchetto:

`cradle sql flush {{pacchetto}}`

- Popola le tabelle per tutti i pacchetti:

`cradle sql populate`

- Popola le tabelle per uno specifico pacchetto:

`cradle sql populate {{pacchetto}}`
