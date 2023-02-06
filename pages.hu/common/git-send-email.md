# git send-email

> Foltok gyűjteményének e-mailben történő elküldése. A foltok megadhatók fájlként, irányként vagy revíziós listaként. További információ: <https://git-scm.com/docs/git-send-email>.

- Az aktuális ág utolsó commitjának elküldése:

`git send-email -1`

- Egy adott commit elküldése:

`git send-email -1 {{commit}}`

- Több (pl. 10) commit küldése az aktuális ágban:

`git send-email {{-10}}`

- Küldjön egy bevezető e-mail üzenetet a javítássorozathoz:

`git send-email -{{number_of_commits}} --compose`

- Az egyes elküldendő javításokhoz tartozó e-mail üzenetek áttekintése és szerkesztése:

`git send-email -{{number_of_commits}} --annotate`
