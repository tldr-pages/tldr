# choco info

> Wyświetlanie szczegółowych informacji o pakiecie Chocolatey.
> Więcej informacji: <https://chocolatey.org/docs/commands-info>.

- Wyświetlanie informacji dotyczących podanego pakietu:

`choco info {{pakiet}}`

- Wyświetlanie informacji dotyczących podanego pakietu zainstalowanego lokalnie:

`choco info {{pakiet}} --local-only`

- Ustawienie określonego źródła/repozytorium pakietów z którego pobrane zostaną informacje:

`choco info {{pakiet}} --source {{adres_url|alias}}`

- Podanie nazwy użytkownika i hasła do uwierzytelnienia:

`choco info {{pakiet}} --user {{nazwa_użytkownika}} --password {{hasło}}`
