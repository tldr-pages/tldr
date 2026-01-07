# choco search

> Wyszukiwanie pakietów Chocolatey dostępnych lokalnie lub w zdalnych źródłach/repozytoriach.
> Więcej informacji: <https://docs.chocolatey.org/en-us/choco/commands/search/>.

- Wyszkukiwanie pakietów:

`choco search {{kwerenda}}`

- Wyszkukiwanie lokalnych pakietów:

`choco search {{kwerenda}} --local-only`

- Wyświetlanie wyłącznie dokładnych dopasowań do podanej kwerendy/szukanej frazy:

`choco search {{kwerenda}} {{[-e|--exact]}}`

- Automatyczna akceptacja wszystkich monitów (--yes):

`choco search {{kwerenda}} {{[-y|--yes]}}`

- Ustawienie określonego źródła do wyszukiwania pakietów:

`choco search {{kwerenda}} {{[-s|--source]}} {{adres_url|alias}}`

- Podanie nazwy użytkownika i hasła do uwierzytelnienia:

`choco search {{kwerenda}} {{[-u|--user]}} {{nazwa_użytkownika}} {{[-p|--password]}} {{hasło}}`
