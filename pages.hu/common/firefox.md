# firefox

> Ingyenes és nyílt forráskódú webböngésző. További információ: <https://developer.mozilla.org/en-US/docs/Mozilla/Command_Line_Options>.

- Indítsa el a Firefoxot, és nyisson meg egy weboldalt:

`firefox {{https://www.duckduckgo.com}}`

- Új ablak megnyitása:

`firefox --new-window {{https://www.duckduckgo.com}}`

- Nyisson meg egy privát (inkognitó) ablakot:

`firefox --private-window`

- Keressen rá a "wikipedia" kifejezésre az alapértelmezett keresőmotorral:

`firefox --search "{{wikipedia}}"`

- Indítsa el a Firefoxot csökkentett módban, minden bővítményt letiltva:

`firefox --safe-mode`

- Készítsen képernyőképet egy weboldalról fej nélküli módban:

`firefox --headless --screenshot {{path/to/output_file.png}} {{https://example.com/}}`

- Egy adott profil használatával a Firefox több különálló példányának egyidejű futtatását engedélyezheti:

`firefox --profile {{path/to/directory}} {{https://example.com/}}`

- A Firefox beállítása alapértelmezett böngészőnek:

`firefox --setDefaultBrowser`
