# attrib

> Fájlok vagy könyvtárak attribútumainak megjelenítése vagy módosítása. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/attrib>.

- Az aktuális könyvtárban lévő fájlok összes beállított attribútumának megjelenítése:

`attrib`

- Egy adott könyvtárban lévő fájlok összes beállított attribútumának megjelenítése:

`attrib {{path\to\directory}}`

- Az aktuális könyvtárban lévő fájlok és \[d\]irectories összes beállított attribútumának megjelenítése:

`attrib /d`

- Az aktuális könyvtárban lévő fájlok és \[s\]ub-könyvtárak összes beállított attribútumának megjelenítése:

`attrib /s`

- A `[r]ead-only` vagy `[a]rchive` vagy `[s]ystem` vagy `[h]idden` vagy `not content [i]ndexed` attribútum hozzáadása fájlokhoz vagy könyvtárakhoz:

`attrib +{{r|a|s|h|i}} {{path\to\file_or_directory1 path\to\file_or_directory2 ...}}`

- A fájlok vagy könyvtárak egy adott attribútumának eltávolítása:

`attrib -{{r|a|s|h|i}} {{path\to\file_or_directory1 path\to\file_or_directory2 ...}}`
