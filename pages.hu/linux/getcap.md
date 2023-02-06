# getcap

> Az egyes megadott fájlok nevének és képességeinek megjelenítésére szolgáló parancs. További információ: <https://manned.org/getcap>.

- A megadott fájlok képességeinek lekérdezése:

`getcap {{path/to/file1 path/to/file2 ...}}`

- A megadott könyvtárak alatt rekurzívan található összes fájl képességeinek lekérdezése:

`getcap -r {{path/to/directory1 path/to/directory2 ...}}`

- Megjeleníti az összes keresett bejegyzést, még akkor is, ha nincsenek képességek megadva:

`getcap -v {{path/to/file1 path/to/file2 ...}}`
