# choco apikey

> Zarządzanie kluczami API dla żródeł Chocolatey.
> Więcej informacji: <https://docs.chocolatey.org/en-us/create/commands/api-key/>.

- Wyświetlanie listy żródeł wraz z kluczami API:

`choco apikey`

- Wyświetlanie konkrentego źródła wraz z kluczem API:

`choco apikey {{[-s|--source]}} "{{adres_url}}"`

- Ustawienie klucza API dla podanego źródła:

`choco apikey {{[-s|--source]}} "{{adres_url}}" {{[-k|--api-key]}} "{{klucz_api}}"`

- Usuwanie klucza API dla podanego źródła:

`choco apikey {{[-s|--source]}} "{{adres_url}}" --remove`
