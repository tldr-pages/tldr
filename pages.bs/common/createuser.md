# createuser

> Napravi PostgreSQL koristnika (uloga).
> Više informacija: <https://www.postgresql.org/docs/current/app-createuser.html>.

- Stvori koristnika interaktivno:

`createuser --interactive {{korisničko_ime}}`

- Stvori koristnika bez posebnih prava:

`createuser {{korisničko_ime}}`

- Stvori superkoristnika:

`createuser {{[-s|--superuser]}} {{korisničko_ime}}`

- Stvori koristnika koji može stvoriti baze podataka, upravjati ulogama i zatraži lozinku:

`createuser {{[-d|--createdb]}} {{[-r|--createrole]}} {{[-P|--pwprompt]}} {{korisničko_ime}}`

- Stvori koristnika bez mogućnosti stvaranja baza podataka ili upravljanja ulogama:

`createuser {{[-D|--no-createdb]}} {{[-R|--no-createrole]}} {{korisničko_ime}}`
