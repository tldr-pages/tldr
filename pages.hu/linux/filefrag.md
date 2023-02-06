# filefrag

> Jelentse, hogy egy adott fájl mennyire töredezett. További információ: <https://manned.org/filefrag>.

- Egy adott fájlra vonatkozó jelentés megjelenítése:

`filefrag {{path/to/file}}`

- Jelentés megjelenítése a fájlok szóközzel elválasztott listájához:

`filefrag {{path/to/file1}} {{path/to/file2}}`

- Jelentés megjelenítése 1024 bájtos blokkmérettel:

`filefrag -b {{path/to/file}}`

- Szinkronizálja a fájlt a leképezés kérése előtt:

`filefrag -s {{path/to/files}}`

- Kiterjesztett attribútumok leképezésének megjelenítése:

`filefrag -x {{path/to/files}}`

- Jelentés megjelenítése részletes információkkal:

`filefrag -v {{path/to/files}}`
