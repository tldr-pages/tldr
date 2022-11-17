# choco apikey

> Zarządzanie kluczami API dla żródeł Chocolatey.
> Więcej informacji: <https://chocolatey.org/docs/commands-apikey>.

- Wyświetlanie listy żródeł wraz z kluczami API:

`choco apikey`

- Wyświetlanie konkrentego źródła wraz z kluczem API:

`choco apikey --source "{{adres_url}}"`

- Ustawienie klucza API dla podanego źródła:

`choco apikey --source "{{adres_url}}" --key "{{klucz_api}}"`

- Usuwanie klucza API dla podanego źródła:

`choco apikey --source "{{adres_url}}" --remove`
