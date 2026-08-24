# choco info

> Wyświetlanie szczegółowych informacji o pakiecie Chocolatey.
> Więcej informacji: <https://docs.chocolatey.org/en-us/choco/commands/info/>.

- Wyświetlanie informacji dotyczących podanego pakietu:

`choco info {{pakiet}}`

- Wyświetlanie informacji dotyczących podanego pakietu zainstalowanego lokalnie:

`choco info {{pakiet}} {{[-l|--local-only]}}`

- Ustawienie określonego źródła/repozytorium pakietów z którego pobrane zostaną informacje:

`choco info {{pakiet}} {{[-s|--source]}} {{adres_url|alias}}`

- Podanie nazwy użytkownika i hasła do uwierzytelnienia:

`choco info {{pakiet}} {{[-u|--user]}} {{nazwa_użytkownika}} {{[-p|--password]}} {{hasło}}`
