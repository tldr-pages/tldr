# groff

> A `troff` és a `nroff` tipizáló segédprogramok GNU helyettesítője. További információ: <https://www.gnu.org/software/groff>.

- Kimenet formázása PostScript nyomtatóhoz, a kimenet mentése egy fájlba:

`groff {{path/to/input.roff}} > {{path/to/output.ps}}`

- Egy man page kiadása az ASCII kimeneti eszközzel, és megjelenítése egy lapozóval:

`groff -man -T ascii {{path/to/manpage.1}} | less --RAW-CONTROL-CHARS`

- Egy man-oldal HTML-fájlba való átfordítása:

`groff -man -T html {{path/to/manpage.1}} > {{path/to/manpage.html}}`

- Egy \[t\]ableseket és \[p\]ikonokat tartalmazó roff-fájl gépelése a \[me\] makrokészlet használatával PDF-be, a kimenet mentése:

`groff {{-t}} {{-p}} -{{me}} -T {{pdf}} {{path/to/input.me}} > {{path/to/output.pdf}}`

- A `groff` parancs futtatása a `grog` segédprogram által kitalált preprocesszor- és makróopciókkal:

`eval "$(grog -T utf8 {{path/to/input.me}})"`
