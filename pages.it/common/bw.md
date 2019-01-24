# bw

> CLI per accedere e gestire vault Bitwarden.

- Esegui il login ad un account Bitwarden:

`bw login`

- Esegui il logout da un account Bitwarden:

`bw logout`

- Cerca e mostra oggetti in un vault Bitwarden:

`bw list items --search {{github}}`

- Mostra un particolare oggetto contenuto in un vault Bitwarden:

`bw get item {{github}}`

- Crea una cartella in un vault bitwarden:

`{{echo -n '{"name":"Nome cartella"}' | base64}} | bw create folder`
