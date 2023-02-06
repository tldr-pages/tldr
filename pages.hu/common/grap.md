# grap

> A groff (GNU Troff) dokumentumformázó rendszer grafikus előfeldolgozója. Lásd még: `pic` és `groff`. További információ: <https://manned.org/grap>.

- A `grap` fájl feldolgozása és a kimeneti fájl mentése későbbi feldolgozásra a `pic` és a `groff` segítségével:

`grap {{path/to/input.grap}} > {{path/to/output.pic}}`

- A \[me\] makrócsomag segítségével a `grap` fájl tipizálása PDF-be, a kimenet mentése egy fájlba:

`grap {{path/to/input.grap}} | pic -T {{pdf}} | groff -{{me}} -T {{pdf}} > {{path/to/output.pdf}}`
