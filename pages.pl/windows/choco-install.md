# choco install

> Instalacja jednej lub więcej paczek zarządzanych przez Chocolatey.
> Więcej informacji: <https://chocolatey.org/docs/commands-install>.

- Instalacja jednego lub więcej pakietów (oddzielonych spacją):

`choco install {{nazwa_pakietu(pakietów)}}`

- Instakacja pakietów z użyciem podanego pliku konfiguracyjnego:

`choco install {{ścieżka/do/plik_konfiguracyjny.config}}`

- Instalacja podanej specyfikacji nuspec lub pliku nupkg:

`choco install {{ścieżka/do/pliku}}`

- Instalacja konkretnej podanej wersji pakietu:

`choco install {{pakiet}} --version {{wersja}}`

- Zezwól na instalacjie wielu wersji danego pakietu:

`choco install {{pakiet}} --allow-multiple`

- Automatyczna akceptacja wszystkich monitów podczas instalacji:

`choco install {{pakiet}} --yes`

- Ustawienie określonego źródła/repozytorium pakietów:

`choco install {{pakiet}} --source {{adres_url|alias}}`

- Podanie nazwy użytkownika i hasła do uwierzytelnienia:

`choco install {{pakiet}} --user {{nazwa_użytkownika}} --password {{hasło}}`
