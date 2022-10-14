# choco upgrade

> Aktualizacja jednej lub więcej paczek zarządzanych przez Chocolatey.
> Więcej informacji: <https://chocolatey.org/docs/commands-upgrade>.

- Aktualizacja jednego lub więcej pakietów (oddzielonych spacją):

`choco upgrade {{nazwa_pakietu(pakietów)}}`

- Aktualizacja pakietu do konkretnej wersji:

`choco upgrade {{nazwa_pakietu(pakietów)}}`

- Aktualizacja wszystkich pakietów zarządzanych przez Chocolatey:

`choco upgrade all`

- Aktualizacja wszystkich pakietów zarządzanych przez Chocolatey z wyjątkiem podanych w parametrze --except:

`choco upgrade all --except "{{nazwa_pomijanego_pakietu(pakietów)}}"`

- Automatyczna akceptacja wszystkich monitów podczas aktualizacji pakietu (--yes):

`choco upgrade {{nazwa_pakietu(pakietów)}} --yes`

- Ustawienie określonego źródła/repozytorium pakietów:

`choco upgrade {{nazwa_pakietu(pakietów)}} --source {{adres_url|alias}}`

- Podanie nazwy użytkownika i hasła do uwierzytelnienia:

`choco upgrade {{nazwa_pakietu(pakietów)}} --user {{nazwa_użytkownika}} --password {{hasło}}`
