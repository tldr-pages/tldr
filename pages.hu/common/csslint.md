# csslint

> CSS kódok lintere. További információ: <https://github.com/CSSLint/csslint/wiki/Command-line-interface>.

- Egyetlen CSS-fájl linternek:

`csslint {{file.css}}`

- Több CSS fájl futtatása:

`csslint {{file1.css}} {{file2.css}} {{file3.css}}`

- Az összes lehetséges stílusszabály listázása:

`csslint --list-rules`

- Bizonyos szabályok hibaként való megadása (amelyek nem nulla kilépési kódot eredményeznek):

`csslint --errors={{errors,universal-selector,imports}} {{file.css}}`

- Bizonyos szabályok figyelmeztetésként való megadása:

`csslint --warnings={{box-sizing,selector-max,floats}} {{file.css}}`

- Bizonyos szabályok figyelmen kívül hagyása:

`csslint --ignore={{ids,rules-count,shorthand}} {{file.css}}`
