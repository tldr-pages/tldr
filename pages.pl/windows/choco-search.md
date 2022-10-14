# choco search

> Wyszukiwanie pakietów Chocolatey dostępnych lokalnie lub w zdalnych źródłach/repozytoriach.
> Więcej informacji: <https://chocolatey.org/docs/commands-search>.

- Wyszkukiwanie pakietów:

`choco search {{kwerenda(szukana_fraza)}}`

- Wyszkukiwanie lokalnych pakietów:

`choco search {{kwerenda(szukana_fraza)}} --local-only`

- Wyświetlanie wyłącznie dokładnych dopasowań do podanej kwerendy/szukanej frazy:

`choco search {{kwerenda(szukana_fraza)}} --exact`

- Automatyczna akceptacja wszystkich monitów (--yes):

`choco search {{kwerenda(szukana_fraza)}} --yes`

- Ustawienie określonego źródła do wyszukiwania pakietów:

`choco search {{kwerenda(szukana_fraza)}} --source {{adres_url|alias}}`

- Podanie nazwy użytkownika i hasła do uwierzytelnienia:

`choco search {{kwerenda(szukana_fraza)}} --user {{nazwa_użytkownika}} --password {{hasło}}`
