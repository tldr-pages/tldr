# sdiff

> 2 fájl közötti különbségek összehasonlítása és opcionálisan egyesítése. További információ: <https://manned.org/sdiff>.

- 2 fájl összehasonlítása:

`sdiff {{path/to/file1}} {{path/to/file2}}`

- 2 fájl összehasonlítása, figyelmen kívül hagyva minden tabulátort és szóközt:

`sdiff -W {{path/to/file1}} {{path/to/file2}}`

- 2 fájl összehasonlítása, figyelmen kívül hagyva a sorok végén lévő szóközöket:

`sdiff -Z {{path/to/file1}} {{path/to/file2}}`

- 2 fájl összehasonlítása a nagy- és kisbetűket figyelmen kívül hagyva:

`sdiff -i {{path/to/file1}} {{path/to/file2}}`

- Összehasonlítás, majd egyesítés, a kimenetet egy új fájlba írva:

`sdiff -o {{path/to/merged_file}} {{path/to/file1}} {{path/to/file2}}`
