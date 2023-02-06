# where

> A keresési mintának megfelelő fájlok helyének megjelenítése. Alapértelmezés szerint az aktuális munkakönyvtár és a PATH környezeti változóban szereplő elérési utak. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/where>.

- A fájlminta helyének megjelenítése:

`where {{file_pattern}}`

- A fájlminta helyének megjelenítése, beleértve a fájl méretét és dátumát:

`where /T {{file_pattern}}`

- Rekurzív keresés a megadott elérési útvonalon található fájlmintára:

`where /R {{path/to/directory}} {{file_pattern}}`

- A fájlminta helyének hibakódjának csendes visszaadása:

`where /Q {{file_pattern}}`
