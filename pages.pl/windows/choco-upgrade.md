# choco upgrade

> Aktualizacja jednej lub więcej paczek zarządzanych przez Chocolatey.
> Więcej informacji: <https://chocolatey.org/docs/commands-upgrade>.

- Aktualizacja jednego lub więcej pakietów (oddzielonych spacją):

`choco upgrade {{pakiet(pakietów)}}`

- Aktualizacja pakietu do konkretnej wersji:

`choco upgrade {{pakiet}}`

- Aktualizacja wszystkich pakietów zarządzanych przez Chocolatey:

`choco upgrade all`

- Uaktualnij wszystkie pakiety z wyjątkiem określonych pakietów rozdzielanych przecinkami:

`choco upgrade all --except "{{pakiet(pakietów)}}"`

- Automatyczna akceptacja wszystkich monitów podczas aktualizacji pakietu (--yes):

`choco upgrade {{pakiet}} --yes`

- Ustawienie określonego źródła/repozytorium pakietów:

`choco upgrade {{pakiet}} --source {{adres_url|alias}}`

- Podanie nazwy użytkownika i hasła do uwierzytelnienia:

`choco upgrade {{pakiet}} --user {{nazwa_użytkownika}} --password {{hasło}}`
