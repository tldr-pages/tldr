# highlight

> A szintaxis-kiemelt forráskódot különböző formátumokban adja ki. További információ: <http://www.andre-simon.de/doku/highlight/highlight.php>.

- Teljes HTML-dokumentum előállítása forráskódfájlból:

`highlight --out-format={{html}} --style {{theme_name}} --syntax {{language}} {{path/to/source_code}}`

- HTML-töredék előállítása, amely alkalmas egy nagyobb dokumentumba való beillesztésre:

`highlight --out-format={{html}} --fragment --syntax {{language}} {{source_file}}`

- Inline CSS-stilizálás minden tagben:

`highlight --out-format={{html}} --inline-css --syntax {{language}} {{source_file}}`

- Az összes támogatott nyelv, téma vagy bővítmény felsorolása:

`highlight --list-scripts {{langs|themes|plugins}}`

- Egy téma CSS-stíluslapjának kinyomtatása:

`highlight --out-format={{html}} --print-style --style {{theme_name}} --syntax {{language}}] --stdout`
