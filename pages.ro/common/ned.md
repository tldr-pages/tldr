# ned

> Este ca `grep`, dar cu capacități puternice de înlocuire.
> Spre deosebire de `sed`, deoarece nu se limitează la editarea orientată spre linie.
> Mai multe informaţii: <https://github.com/nevdelap/ned>

- Caută recursiv pornind de la directorul curent, ignorând cazul:

`ned --ignore-case --recursive '{{^[dl]og}}' {{.}}`

- Caută întotdeauna afișarea de ieșire colorată:

`ned --colors '{{^[dl]og}}' {{.}}`

- Căutare care nu arată niciodată culoarea de ieșire:

`ned --colors=never '{{^[dl]og}}' {{.}}`

- Caută ignorând anumite fișiere:

`ned --recursive --exclude '{{*.htm}}' '{{^[dl]og}}' {{.}}`

- Înlocuire simplă:

`ned '{{dog}}' --replace '{{cat}}' {{.}}`

- Înlocuiți folosind referințe de grup numerotate:

`ned '{{the ([a-z]+) dog and the ([a-z]+) dog}}' --replace '{{the $2 dog and the $1 dog}}' {{.}}`

- Înlocuiți schimbarea cazului:

`ned '{{([a-z]+) dog}}' --case-replacements --replace '{{\U$1\E! dog}}' --stdout {{.}}`

- Previzualizați rezultatele unei găsi și înlocuiți fără actualizarea fișierelor țintă:

`ned '{{^[sb]ad}}' --replace '{{happy}}' --stdout {{.}}`
