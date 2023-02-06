# s

> Webes keresés a terminálról. További információ: <https://github.com/zquestz/s>.

- Keresés egy lekérdezésre a Google-on (alapértelmezett szolgáltató):

`s {{query}}`

- Az összes szolgáltató felsorolása:

`s --list-providers`

- Keresés egy lekérdezésre egy adott szolgáltatóval:

`s --provider {{provider}} {{query}}`

- Egy megadott bináris szolgáltató használata a keresési lekérdezés végrehajtásához:

`s --binary "{{binary}} {{arguments}}" {{query}}`
