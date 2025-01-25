# scoop bucket

> Zarządzaj bucketami: repozytoriami Git zawierającymi pliki, które opisują sposób instalacji aplikacji przez Scoop.
> Jeśli Scoop nie zna lokalizacji bucketa, należy określić lokalizację jego repozytorium.
> Więcej informacji: <https://github.com/lukesampson/scoop/wiki/Buckets>.

- Wyświetl wszystkie aktualnie używane buckety:

`scoop bucket list`

- Wyświetl wszystkie znane buckety:

`scoop bucket known`

- Dodaj znany bucket według jego nazwy:

`scoop bucket add {{nazwa}}`

- Dodaj nieznany bucket według jego nazwy i adresu URL repozytorium Git:

`scoop bucket add {{nazwa}} {{https://example.com/repository.git}}`

- Usuń bucket według jego nazwy:

`scoop bucket rm {{nazwa}}`
