# choco search

> Wyszukiwanie pakietów Chocolatey dostępnych lokalnie lub w zdalnych źródłach/repozytoriach.
> Więcej informacji: <https://chocolatey.org/docs/commands-search>.

- Wyszkukiwanie pakietów:

`choco search {{kwerenda}}`

- Wyszkukiwanie lokalnych pakietów:

`choco search {{kwerenda}} --local-only`

- Wyświetlanie wyłącznie dokładnych dopasowań do podanej kwerendy/szukanej frazy:

`choco search {{kwerenda}} --exact`

- Automatyczna akceptacja wszystkich monitów (--yes):

`choco search {{kwerenda}} --yes`

- Ustawienie określonego źródła do wyszukiwania pakietów:

`choco search {{kwerenda}} --source {{adres_url|alias}}`

- Podanie nazwy użytkownika i hasła do uwierzytelnienia:

`choco search {{kwerenda}} --user {{nazwa_użytkownika}} --password {{hasło}}`
