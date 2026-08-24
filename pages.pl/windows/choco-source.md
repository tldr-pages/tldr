# choco source

> Zarządzaj źródłami/repozytoriami pakietów Chocolatey.
> Więcej informacji: <https://docs.chocolatey.org/en-us/choco/commands/source/>.

- Wyświetl aktualnie dostępne źródła:

`choco source list`

- Dodaj nowe źródło:

`choco source add {{[-n|--name]}} {{nazwa}} {{[-s|--source]}} {{adres_url}}`

- Dodaj nowe źródło z użyciem poświadczeń:

`choco source add {{[-n|--name]}} {{nazwa}} {{[-s|--source]}} {{adres_url}} {{[-u|--user]}} {{nazwa_użytkownika}} {{[-p|--password]}} {{hasło}}`

- Dodaj nowe źródło z użyciem certyfikatu:

`choco source add {{[-n|--name]}} {{nazwa}} {{[-s|--source]}} {{adres_url}} --cert {{ścieżka/do/certyfikatu}}`

- Włącz dane źródło/repozytorium pakietów:

`choco source enable {{[-n|--name]}} {{nazwa}}`

- Wyłącz dane źródło/repozytorium pakietów:

`choco source disable {{[-n|--name]}} {{nazwa}}`

- Usuń dane źródło/repozytorium:

`choco source remove {{[-n|--name]}} {{nazwa}}`
