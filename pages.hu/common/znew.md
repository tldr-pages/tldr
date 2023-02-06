# znew

> Fájlok újratömörítése a `.Z` formátumból a `.gz` formátumba. További információ: <https://manned.org/znew>.

- Fájlok újratömörítése a `.Z` formátumból a `.gz` formátumba:

`znew {{path/to/file1.Z}}`

- Több fájl újratömörítése és az elért méretcsökkentési % megjelenítése fájlonként:

`znew -v {{path/to/file1.Z}} {{path/to/file2.Z}} {{path/to/file3.Z}}`

- Egy fájl újratömörítése a leglassabb tömörítési módszerrel (az optimális tömörítés érdekében):

`znew -9 {{path/to/file1.Z}}`

- Újratömörít egy fájlt, \[K\]eenntartva a `.Z` fájlt, ha az kisebb, mint a `.gz` fájl:

`znew -K {{path/to/file1.Z}}`
