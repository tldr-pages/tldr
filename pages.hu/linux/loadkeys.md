# loadkeys

> A konzol kernel billentyűzettérképének betöltése. További információ: <https://manned.org/loadkeys>.

- Alapértelmezett billentyűzettérkép betöltése:

`loadkeys --default`

- Alapértelmezett billentyűzettérkép betöltése, ha szokatlan billentyűzettérkép van betöltve, és a `-` jel nem található:

`loadkeys defmap`

- A kernel forrástáblázatának létrehozása:

`loadkeys --mktable`

- Bináris keymap létrehozása:

`loadkeys --bkeymap`

- Keymap keresése és elemzése művelet nélkül:

`loadkeys --parse`

- A keymap betöltése minden kimenetet elnyomva:

`loadkeys --quiet`

- Keymap betöltése a megadott fájlból a konzol számára:

`loadkeys --console {{/dev/ttyN}} {{/path/to/file}}`

- Szabványos nevek használata a különböző nyelvi tartományok billentyűzettérképeihez:

`loadkeys --console {{/dev/ttyN}} {{uk}}`
