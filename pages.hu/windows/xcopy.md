# xcopy

> Fájlok és könyvtárfák másolása. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/xcopy>.

- A fájl(ok) másolása a megadott célállomásra:

`xcopy {{path/to/file_or_directory}} {{path/to/destination}}`

- A másolás előtt listázza a másolandó fájlokat:

`xcopy {{path/to/file_or_directory}} {{path/to/destination}} /p`

- Csak a könyvtárszerkezet másolása, a fájlok kivételével:

`xcopy {{path/to/file_or_directory}} {{path/to/destination}} /t`

- Üres könyvtárak bevonása másoláskor:

`xcopy {{path/to/file_or_directory}} {{path/to/destination}} /e`

- A forrás ACL megtartása a célállomásban:

`xcopy {{path/to/file_or_directory}} {{path/to/destination}} /o`

- A folytatás engedélyezése a hálózati kapcsolat megszakadása esetén:

`xcopy {{path/to/file_or_directory}} {{path/to/destination}} /z`

- Tiltja a kérést, ha a fájl létezik a célállomáson:

`xcopy {{path/to/file_or_directory}} {{path/to/destination}} /y`

- Részletes használati információk megjelenítése:

`xcopy /?`
