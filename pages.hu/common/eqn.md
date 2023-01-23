# eqn

> Egyenlet preprocesszor a groff (GNU Troff) dokumentumformázó rendszerhez. Lásd még: `troff` és `groff`. További információ: <https://manned.org/eqn>.

- Feldolgozza a bemenetet egyenletekkel, a kimenetet pedig elmenti a későbbi, groff-al történő szedéshez PostScript-be:

`eqn {{path/to/input.eqn}} > {{path/to/output.roff}}`

- Egy egyenleteket tartalmazó bemeneti fájl gépelése PDF-be a \[me\] makrócsomag segítségével:

`eqn -T {{pdf}} {{path/to/input.eqn}} | groff -{{me}} -T {{pdf}} > {{path/to/output.pdf}}`
