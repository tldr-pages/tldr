# jrnl

> Una semplice applicazione da linea di comando per tenere un diario.
> Maggiori informazioni: <http://jrnl.sh>.

- Inserisci una nuova nota con il tuo editor:

`jrnl`

- Inserimento veloce di una nota:

`jrnl {{today at 3am}}: {{titolo}}. {{contenuto}}`

- Mostra le ultime dieci note inserite:

`jrnl -n {{10}}`

- Mostra tutto quello che è successo dall'inizio dello scorso anno fino all'inizio di marzo:

`jrnl -from "{{last year}}" -until {{march}}`

- Modifica tutte le note taggate con "texas" e "history":

`jrnl {{@texas}} -and {{@history}} --edit`
