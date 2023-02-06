# install

> Fájlok másolása és attribútumok beállítása. Fájlok (gyakran futtatható) másolása egy rendszerhelyre, például a `/usr/local/bin`, a megfelelő engedélyek/tulajdonjogok megadása. További információ: <https://www.gnu.org/software/coreutils/install>.

- Fájlok másolása a célállomásra:

`install {{path/to/source_file1 path/to/source_file2 ...}} {{path/to/destination}}`

- Fájlok másolása a célállomásra, tulajdonjoguk beállítása:

`install --owner {{user}} {{path/to/source_file1 path/to/source_file2 ...}} {{path/to/destination}}`

- Fájlok másolása a célállomásra, csoporttulajdonlásuk beállítása:

`install --group {{user}} {{path/to/source_file1 path/to/source_file2 ...}} {{path/to/destination}}`

- Fájlok másolása a célállomásra, beállításuk `mode`:

`install --mode {{+x}} {{path/to/source_file1 path/to/source_file2 ...}} {{path/to/destination}}`

- Fájlok másolása és a forrás hozzáférési/módosítási idejének alkalmazása a célállomásra:

`install --preserve-timestamps {{path/to/source_file1 path/to/source_file2 ...}} {{path/to/destination}}`

- Fájlok másolása és a könyvtárak létrehozása a célállomáson, ha azok nem léteznek:

`install -D {{path/to/source_file1 path/to/source_file2 ...}} {{path/to/destination}}`
