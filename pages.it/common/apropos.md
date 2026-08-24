# apropos

> Cerca nomi e descrizioni nelle pagine di manuale.
> Vedi anche: `man`.
> Maggiori informazioni: <https://manned.org/apropos>.

- Cerca una parola chiave usando `regex`:

`apropos {{regex}}`

- Cerca senza limitare l'output alla larghezza del terminale (output lungo):

`apropos {{[-l|--long]}} {{regex}}`

- Cerca pagine che corrispondono a tutte le `regex` specificate:

`apropos {{regex_1}} {{[-a|--and]}} {{regex_2}} {{[-a|--and]}} {{regex_3}}`
