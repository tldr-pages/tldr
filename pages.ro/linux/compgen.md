# compgen

> O comandă încorporată pentru auto-completare în bash, care este apelată la apăsarea tastei TAB de două ori.
> Mai multe informaţii: <https://www.gnu.org/software/bash/manual/bash.html#index-compgen>

- Listați toate comenzile pe care le puteți executa:

`compgen -c`

- Listează toate pseudonimele:

`compgen -a`

- Listați toate funcțiile pe care le puteți executa:

`compgen -A function`

- Arată cuvinte cheie rezervate coajă:

`compgen -k`

- Vezi toate comenziile/pseudonimele disponibile începând cu „ls”:

`compgen -ac {{ls}}`
