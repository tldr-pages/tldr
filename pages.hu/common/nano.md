# nano

> Parancssori szövegszerkesztő. Továbbfejlesztett `Pico` klón. További információ: <https://nano-editor.org>.

- Indítsa el a szerkesztőt:

`nano`

- A szerkesztő elindítása konfigurációs fájlok használata nélkül:

`nano --ignorercfiles`

- Meghatározott fájlok megnyitása, a következő fájlra való áttérés az előző bezárásakor:

`nano {{path/to/file1 path/to/file2 ...}}`

- Fájl megnyitása és a kurzor meghatározott sorra és oszlopra történő pozícionálása:

`nano +{{line}},{{column}} {{path/to/file}}`

- Fájl megnyitása és a soft wrapping engedélyezése:

`nano --softwrap {{path/to/file}}`

- Fájl megnyitása és az új sorok behúzása az előző sor behúzásához:

`nano --autoindent {{path/to/file}}`

- Fájl megnyitása és mentéskor biztonsági másolat létrehozása (`path/to/file~`):

`nano --backup {{path/to/file}}`
