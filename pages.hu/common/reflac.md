# reflac

> FLAC fájlok helyben történő újratömörítése a metaadatok megőrzése mellett. További információ: <https://github.com/chungy/reflac>.

- FLAC fájlokat tartalmazó könyvtár újratömörítése:

`reflac {{path/to/directory}}`

- Maximális tömörítés engedélyezése (nagyon lassú):

`reflac --best {{path/to/directory}}`

- A fájlnevek megjelenítése a feldolgozás során:

`reflac --verbose {{path/to/directory}}`

- Újbóli keresés az alkönyvtárakban:

`reflac --recursive {{path/to/directory}}`

- A fájlok módosítási idejének megőrzése:

`reflac --preserve {{path/to/directory}}`
