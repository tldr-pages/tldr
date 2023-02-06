# troff

> A groff (GNU Troff) dokumentumformázó rendszer tipizáló processzora. Lásd még: `groff`. További információ: <https://manned.org/troff>.

- Kimenet formázása PostScript nyomtatóhoz, a kimenet mentése egy fájlba:

`troff {{path/to/input.roff}} | grops > {{path/to/output.ps}}`

- Kimenet formázása PostScript nyomtatóra a \[me\] makrócsomag használatával, a kimenet mentése egy fájlba:

`troff -{{me}} {{path/to/input.roff}} | grops > {{path/to/output.ps}}`

- Kimenet formázása \[a\]SCII szövegként a \[man\] makrócsomag használatával:

`troff -T {{ascii}} -{{man}} {{path/to/input.roff}} | grotty`

- Kimenet formázása \[pdf\] fájlként, a kimenet mentése fájlba:

`troff -T {{pdf}} {{path/to/input.roff}} | gropdf > {{path/to/output.pdf}}`
