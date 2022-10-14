# choco info

> Wyświetlanie szczegółowych informacji o pakiecie Chocolatey.
> Więcej informacji: <https://chocolatey.org/docs/commands-info>.

- Wyświetlanie informacji dotyczących podanego pakietu:

`choco info {{nazwa_pakietu}}`

- Wyświetlanie informacji dotyczących podanego pakietu zainstalowanego lokalnie:

`choco info {{nazwa_pakietu}} --local-only`

- Ustawienie określonego źródła/repozytorium pakietów z którego pobrane zostaną informacje:

`choco info {{nazwa_pakietu}} --source {{adres_url|alias}}`

- Podanie nazwy użytkownika i hasła do uwierzytelnienia:

`choco info {{nazwa_pakietu}} --user {{nazwa_użytkownika}} --password {{hasło}}`
