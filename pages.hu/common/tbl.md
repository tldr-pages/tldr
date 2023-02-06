# tbl

> A groff (GNU Troff) dokumentumformázó rendszer táblázat-előfeldolgozója. Lásd még: `groff` és `troff`. További információ: <https://manned.org/tbl>.

- Feldolgozza a bemenetet táblázatokkal, a kimenetet pedig elmenti a későbbi, groffal történő szedéshez PostScript-be:

`tbl {{path/to/input_file}} > {{path/to/output.roff}}`

- A \[me\] makrócsomag segítségével a táblázatokkal ellátott bemenet tipizálása PDF-be:

`tbl -T {{pdf}} {{path/to/input.tbl}} | groff -{{me}} -T {{pdf}} > {{path/to/output.pdf}}`
