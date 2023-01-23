# ned

> Olyan, mint a `grep`, de nagy teljesítményű cserélési lehetőségekkel. Ellentétben a `sed`, mivel nem korlátozódik a sororientált szerkesztésre. További információ: <https://github.com/nevdelap/ned>.

- Rekurzív keresés az aktuális könyvtárból kiindulva, figyelmen kívül hagyva az eseteket:

`ned --ignore-case --recursive '{{^[dl]og}}' {{.}}`

- A keresés mindig színes kimenetet mutat:

`ned --colors '{{^[dl]og}}' {{.}}`

- A keresés soha nem mutat színes kimenetet:

`ned --colors=never '{{^[dl]og}}' {{.}}`

- Bizonyos fájlok figyelmen kívül hagyása:

`ned --recursive --exclude '{{*.htm}}' '{{^[dl]og}}' {{.}}`

- Egyszerű csere:

`ned '{{dog}}' --replace '{{cat}}' {{.}}`

- Csere számozott csoporthivatkozásokkal:

`ned '{{the ([a-z]+) dog and the ([a-z]+) dog}}' --replace '{{the $2 dog and the $1 dog}}' {{.}}`

- Cserélje az esetek megváltoztatásával:

`ned '{{([a-z]+) dog}}' --case-replacements --replace '{{\U$1\E! dog}}' --stdout {{.}}`

- Keresés és csere eredményeinek előnézete a célfájlok frissítése nélkül:

`ned '{{^[sb]ad}}' --replace '{{happy}}' --stdout {{.}}`
