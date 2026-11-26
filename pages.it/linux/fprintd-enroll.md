# fprintd-enroll

> Registra le impronte digitali nel database.
> Maggiori informazioni: <https://manned.org/fprintd-enroll>.

- Registra l'indice destro per l'utente corrente:

`fprintd-enroll`

- Registra un dito specifico per l'utente corrente:

`fprintd-enroll {{[-f|--finger]}} {{left-thumb|left-index-finger|left-middle-finger|left-ring-finger|left-little-finger|right-thumb|...}}`

- Registra l'indice destro per un utente specifico:

`fprintd-enroll {{nome_utente}}`

- Registra un dito specifico per un utente specifico:

`fprintd-enroll {{[-f|--finger]}} {{finger_name}} {{nome_utente}}`

- Mostra l'aiuto:

`fprintd-enroll --help`
