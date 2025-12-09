# choco source

> Zarządzaj źródłami/repozytoriami pakietów Chocolatey.
> Więcej informacji: <https://chocolatey.org/docs/commands-source>.

- Wyświetl aktualnie dostępne źródła:

`choco source list`

- Dodaj nowe źródło:

`choco source add --name {{nazwa}} --source {{adres_url}}`

- Dodaj nowe źródło z użyciem poświadczeń:

`choco source add --name {{nazwa}} --source {{adres_url}} --user {{nazwa_użytkownika}} --password {{hasło}}`

- Dodaj nowe źródło z użyciem certyfikatu:

`choco source add --name {{nazwa}} --source {{adres_url}} --cert {{ścieżka/do/certyfikatu}}`

- Włącz dane źródło/repozytorium pakietów:

`choco source enable --name {{nazwa}}`

- Wyłącz dane źródło/repozytorium pakietów:

`choco source disable --name {{nazwa}}`

- Usuń dane źródło/repozytorium:

`choco source remove --name {{nazwa}}`
