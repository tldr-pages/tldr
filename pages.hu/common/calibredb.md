# calibredb

> Eszköz az e-könyv-adatbázis manipulálására. A Calibre e-könyvtár része. További információ: <https://manual.calibre-ebook.com/generated/en/calibredb.html>.

- E-könyvek listázása a könyvtárban további információkkal:

`calibredb list`

- További információkat megjelenítő e-könyvek keresése:

`calibredb list --search {{search_term}}`

- Csak az e-könyvek azonosítóinak keresése:

`calibredb search {{search_term}}`

- Egy vagy több e-könyv hozzáadása a könyvtárhoz:

`calibredb add {{file1 file2 …}}`

- Egy könyvtár alatt található összes e-könyv rekurzív hozzáadása a könyvtárhoz:

`calibredb add -r {{path/to/directory}}`

- Egy vagy több e-könyv eltávolítása a könyvtárból. Szüksége van az e-könyvek azonosítóira (lásd fentebb):

`calibredb remove {{id1 id2 …}}`
