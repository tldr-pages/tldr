# choco source

> Zarządzanie źrółami/repozytorium pakietów Chocolatey.
> Więcej informacji: <https://chocolatey.org/docs/commands-source>.

- Wylistowanie aktualnie dostępmnych źródeł:

`choco source list`

- Dodanie nowego źródła:

`choco source add --name {{nazwa}} --source {{adres_url}}`

- Dodanie nowego źródła z użyciem poświadczeń:

`choco source add --name {{nazwa}} --source {{adres_url}} --user {{nazwa_użytkownika}}} --password {{hasło}}`

- Dodanie nowego źródła z użyciem certyfikatu:

`choco source add --name {{nazwa}} --source {{adres_url}} --cert {{ścieżka/do/certyfikatu}}`

- Włączenie danego źródła/repozytorium pakietów:

`choco source enable --name {{nazwa}}`

- Wyłączenie danego źródła/repozytorium pakietów:

`choco source disable --name {{nazwa}}`

- Usunięcie danego źródła/repozytorium:

`choco source remove --name {{nazwa}}`
