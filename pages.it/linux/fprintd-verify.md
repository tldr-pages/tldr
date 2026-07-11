# fprintd-verify

> Verifica le impronte digitali rispetto al database.
> Maggiori informazioni: <https://manned.org/fprintd-verify>.

- Verifica tutte le impronte digitali memorizzate per l'utente corrente:

`fprintd-verify`

- Verifica un'impronta digitale specifica per l'utente corrente:

`fprintd-verify {{[-f|--finger]}} {{left-thumb|left-index-finger|left-middle-finger|left-ring-finger|left-little-finger|right-thumb|...}}`

- Verifica le impronte digitali per un utente specifico:

`fprintd-verify {{username}}`

- Verifica un'impronta digitale specifica per un utente specifico:

`fprintd-verify {{[-f|--finger]}} {{finger_name}} {{username}}`

- Fallisce il processo se un'impronta digitale non corrisponde a quelle memorizzate nel database per l'utente corrente:

`fprintd-verify --g-fatal-warnings`

- Mostra aiuto:

`fprintd-verify {{[-h|--help]}}`
