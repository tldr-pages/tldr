# unzipsfx

> Önkicsomagoló tömörített bináris fájl létrehozása a `zip` fájl önkitömörítő csonkjainak előfűzésével. További információ: <https://manned.org/unzipsfx>.

- Önkicsomagoló bináris fájl létrehozása a `zip` archívumból:

`cat unzipsfx {{path/to/archive.zip}} > {{filename}} && chmod 755 {{filename}}`

- Önkicsomagoló bináris fájl kicsomagolása az aktuális könyvtárban:

`{{./path/to/binary)}}`

- Önkicsomagoló bináris állomány tesztelése hibák szempontjából:

`{{./path/to/binary)}} -t`

- Az önkicsomagoló bináris fájl tartalmának kinyomtatása kicsomagolás nélkül:

`{{./path/to/binary)}} -c {{path/to/filename}}`

- A `zip` archívumhoz tartozó megjegyzések kinyomtatása az önkicsomagoló binárisban:

`{{./path/to/binary)}} -z`
