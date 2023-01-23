# vale

> Bővíthető stílusellenőrző, amely többféle jelölési formátumot támogat, például Markdown és AsciiDoc. További információ: <https://vale.sh>.

- Egy fájl stílusának ellenőrzése:

`vale {{path/to/file}}`

- Egy fájl stílusának ellenőrzése egy megadott konfigurációval:

`vale --config='{{path/to/.vale.ini}}' {{path/to/file}}`

- Az eredmények JSON formátumban történő kiadása:

`vale --output=JSON {{path/to/file}}`

- Stílusproblémák ellenőrzése meghatározott súlyossági szinten és annál magasabb szinten:

`vale --minAlertLeve={{suggestion|warning|error}} {{path/to/file}}`

- A stílus ellenőrzése a `stdin`, a jelölési formátum megadásával:

`cat {{file.md}} | vale --ext=.md`

- Az aktuális konfiguráció listázása:

`vale ls-config`
