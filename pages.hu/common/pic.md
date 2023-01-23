# pic

> Képelőfeldolgozó a groff (GNU Troff) dokumentumformázó rendszerhez. Lásd még: `groff` és `troff`. További információ: <https://manned.org/pic>.

- A bemenetet képekkel dolgozza fel, a kimenetet a későbbi, groffal történő szedéshez PostScript-be mentve:

`pic {{path/to/input.pic}} > {{path/to/output.roff}}`

- A \[me\] makrócsomag segítségével képekkel ellátott bemenet tipizálása PDF-be:

`pic -T {{pdf}} {{path/to/input.pic}} | groff -{{me}} -T {{pdf}} > {{path/to/output.pdf}}`
