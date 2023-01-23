# zfgrep

> Rögzített karakterláncok illesztése esetlegesen tömörített fájlokban. A `grep -F` egyenértékű a szolgáltatással, szükség esetén előbb a bemenetet dekompresszálja. További információ: <https://manned.org/zfgrep>.

- Pontos karakterlánc keresése egy fájlban:

`zfgrep {{search_string}} {{path/to/file}}`

- Megszámolja a megadott karakterláncnak megfelelő sorok számát a fájlban:

`zfgrep --count {{search_string}} {{path/to/file}}`

- Megjeleníti a fájl sorszámát a megfelelő sorokkal együtt:

`zfgrep --line-number {{search_string}} {{path/to/file}}`

- Az összes sor megjelenítése a keresett karakterláncot tartalmazó sorok kivételével:

`zfgrep --invert-match {{search_string}} {{path/to/file}}`

- Csak olyan fájlnevek listázása, amelyek tartalma legalább egyszer megegyezik a keresett karakterlánccal:

`zfgrep --files-with-matches {{search_string}} {{path/to/file1 path/to/file2 ...}}`
