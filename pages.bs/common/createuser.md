# createuser

> Napravi PostgreSQL koristnika (uloga).
> Više Informacija: <https://www.postgresql.org/docs/current/app-createuser.html>.

- Stvori koristnika interaktivno:

`createuser --interactive {{username}}`

- Stvori koristnika bez posebnih prava:

`createuser {{username}}`

- Stvori superkoristnika:

`createuser {{[-s|--superuser]}} {{username}}`

- Stvori koristnika koji može stvoriti baze podataka, upravjati ulogama i zatraži lozinku:

`createuser {{[-d|--createdb]}} {{[-r|--createrole]}} {{[-P|--pwprompt]}} {{username}}`

- Stvori koristnika bez mogućnosti stvaranja baza podataka ili upravljanja ulogama:

`createuser {{[-D|--no-createdb]}} {{[-R|--no-createrole]}} {{username}}`
