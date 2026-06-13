# atq

> Mostra job programmati dai comandi `at` o `batch`.
> Maggiori informazioni: <https://manned.org/atq>.

- Mostra i job programmati per l'utente corrente:

`atq`

- Mostra i job della coda 'a' (le code hanno nomi di un singolo carattere):

`atq -q {{a}}`

- Mostra i job di tutti gli utenti (da eseguire come super user):

`sudo atq`
