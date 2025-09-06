# choco outdated

> Sprawdzenie nieaktualnych pakietów zarządzanych przez Chocolatey.
> Więcej informacji: <https://chocolatey.org/docs/commands-outdated>.

- Wyświetlanie listy nieaktualnych pakietów w formie tabeli:

`choco outdated`

- Pominięcie/ignorowanie obecnie przypiętych pakietów:

`choco outdated --ignore-pinned`

- Ustawienie określonego źródła do sprawdzenia aktualności pakietów:

`choco outdated --source {{adres_url|alias}}`

- Podanie nazwy użytkownika i hasła do uwierzytelnienia:

`choco outdated --user {{nazwa_użytkownika}} --password {{hasło}}`
