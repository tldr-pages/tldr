# idnits

> Ellenőrizze az internetes tervezeteket a benyújtási nittek tekintetében. Keresse a 2.1. és 2.2. pont megsértését a <https://www.ietf.org/id-info/checklist> oldalon felsorolt követelmények közül. További információ: <https://tools.ietf.org/tools/idnits/>.

- Ellenőrizze a fájlokat a hiányosságok szempontjából:

`idnits {{path/to/file.txt}}`

- Megszámolja a nitteket anélkül, hogy megjelenítené őket:

`idnits --nitcount {{path/to/file.txt}}`

- További információk megjelenítése a jogsértő sorokról:

`idnits --verbose {{path/to/file.txt}}`

- A megadott évszámot várja a boilerplate-ben az aktuális évszám helyett:

`idnits --year {{2021}} {{path/to/file.txt}}`

- Feltételezze, hogy a dokumentum a megadott státuszú:

`idnits --doctype {{standard|informational|experimental|bcp|ps|ds}} {{path/to/file.txt}}`
