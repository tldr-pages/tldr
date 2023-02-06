# phpcs

> A PHP, JavaScript és CSS fájlok tokenizálása a kódolási szabványok megsértésének észlelésére. További információ: <https://github.com/squizlabs/PHP_CodeSniffer>.

- A megadott könyvtár szimatolása problémák után (alapértelmezés szerint a PEAR szabvány szerint):

`phpcs {{path/to/directory}}`

- A telepített kódolási szabványok listájának megjelenítése:

`phpcs -i`

- Megad egy kódolási szabványt, amely alapján ellenőrizni kívánja:

`phpcs {{path/to/directory}} --standard {{standard}}`

- A szimatoláskor figyelembe veendő, vesszővel elválasztott fájlkiterjesztések megadása:

`phpcs {{path/to/directory}} --extensions {{file_extension(s)}}`

- A kimeneti jelentés formátumának megadása (pl. `full`, `xml`, `json`, `summary`):

`phpcs {{path/to/directory}} --report {{format}}`

- A folyamat során használandó konfigurációs változók beállítása:

`phpcs {{path/to/directory}} --config-set {{key}} {{value}}`

- A feldolgozás előtt betöltendő fájlok vesszővel elválasztott listája:

`phpcs {{path/to/directory}} --bootstrap {{file(s)}}`

- Ne keressen vissza alkönyvtárakba:

`phpcs {{path/to/directory}} -l`
