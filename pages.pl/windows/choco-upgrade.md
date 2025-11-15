# choco upgrade

> Zaktualizuj jeden lub więcej pakietów Chocolatey.
> Więcej informacji: <https://chocolatey.org/docs/commands-upgrade>.

- Zaktualizuj jeden lub więcej pakietów (oddzielonych spacją):

`choco upgrade {{pakiet1 pakiet2 ...}}`

- Zaktualizuj pakiet do konkretnej wersji:

`choco upgrade {{pakiet}} --version {{wersja}}`

- Zaktualizuj wszystkie pakiety:

`choco upgrade all`

- Zaktualizuj wszystkie pakiety z wyjątkiem tych podanych, rozdzielanych przecinkami:

`choco upgrade all --except "{{pakiet1 pakiet2 ...}}"`

- Automatycznie akceptuj wszystkie monity podczas aktualizacji pakietu:

`choco upgrade {{pakiet}} --yes`

- Ustaw określone źródło/repozytorium pakietów:

`choco upgrade {{pakiet}} --source {{adres_url|alias}}`

- Podaj nazwę użytkownika i hasło do uwierzytelnienia:

`choco upgrade {{pakiet}} --user {{nazwa_użytkownika}} --password {{hasło}}`
