# readpe

> Megjeleníti a PE-fájlokra vonatkozó információkat. További információ: <https://manned.org/readpe>.

- A PE-fájl összes információjának megjelenítése:

`readpe {{path/to/executable}}`

- A PE-fájlban található összes fejléc megjelenítése:

`readpe --all-headers {{path/to/executable}}`

- A PE-fájlban található összes szakasz megjelenítése:

`readpe --all-sections {{path/to/executable}}`

- Egy adott fejléc megjelenítése egy PE-fájlból:

`readpe --header {{dos|coff|optional}} {{path/to/executable}}`

- Az összes importált függvény listázása:

`readpe --imports {{path/to/executable}}`

- Az összes exportált függvény listázása:

`readpe --exports {{path/to/executable}}`
