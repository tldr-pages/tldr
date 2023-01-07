# bw

> CLI per accedere e gestire vault Bitwarden.
> Maggiori informazioni: <https://help.bitwarden.com/article/cli/>.

- Esegui il login ad un account Bitwarden:

`bw login`

- Esegui il logout da un account Bitwarden:

`bw logout`

- Cerca e mostra oggetti in un vault Bitwarden:

`bw list items --search {{github}}`

- Mostra un particolare oggetto contenuto in un vault Bitwarden:

`bw get item {{github}}`

- Crea una directory in un vault bitwarden:

`{{echo -n '{"name":"Nome directory"}' | base64}} | bw create folder`
