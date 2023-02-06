# jrnl

> Egy egyszerű napló alkalmazás a parancssorhoz. További információ [: http://jrnl.sh](http://jrnl.sh).

- Új bejegyzés beillesztése a szerkesztővel:

`jrnl`

- Gyorsan beilleszthet egy új bejegyzést:

`jrnl {{today at 3am}}: {{title}}. {{content}}`

- Az utolsó tíz bejegyzés megtekintése:

`jrnl -n {{10}}`

- Tekintse meg mindazt, ami a tavalyi év elejétől a tavaly március elejéig történt:

`jrnl -from "{{last year}}" -until {{march}}`

- Az összes "texas" és "history" címkével ellátott bejegyzés szerkesztése:

`jrnl {{@texas}} -and {{@history}} --edit`
